"""
GigShield – Disruption Classification Model (XGBoost Classifier)
Classifies real-time environmental data into disruption categories
that trigger parametric payouts.

Labels:
  0 = No Disruption
  1 = Weather Disruption  (rain, wind, low visibility)
  2 = Air Quality Disruption  (AQI > 250)
  3 = Civic Disruption  (strike, protest, curfew, order drop)
  4 = Compound Disruption  (2+ triggers active simultaneously)

Usage:
    python train_disruption_model.py
    python train_disruption_model.py --data data/disruption_data.csv --out models/
"""

import argparse
import os
import json
import joblib
import numpy as np
import pandas as pd

from sklearn.model_selection import train_test_split, StratifiedKFold, cross_val_score
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import (
    accuracy_score, classification_report, confusion_matrix
)
from xgboost import XGBClassifier

# ─── Constants ────────────────────────────────────────────────────────────────
FEATURES = [
    "rainfall_mm_3h",
    "wind_speed_kmh",
    "aqi_value",
    "visibility_km",
    "temp_celsius",
    "civic_event_flag",
    "hour_of_day",
    "is_weekend",
    "platform_order_drop_pct",
]
TARGET = "disruption_label"
LABEL_NAMES = {
    0: "No Disruption",
    1: "Weather Disruption",
    2: "Air Quality Disruption",
    3: "Civic Disruption",
    4: "Compound Disruption",
}

# Payout multipliers per disruption type (used by Flask API for claims)
PAYOUT_MULTIPLIERS = {
    0: 0.0,   # No payout
    1: 1.0,   # 100% of coverage
    2: 0.75,  # 75% of coverage
    3: 0.85,  # 85% of coverage
    4: 1.5,   # 150% (compound — capped at policy max in Spring Boot)
}

# Severity scores (0–1) used by fraud detection model
SEVERITY_SCORES = {0: 0.0, 1: 0.85, 2: 0.70, 3: 0.75, 4: 1.0}


def load_or_generate(data_path: str) -> pd.DataFrame:
    if os.path.exists(data_path):
        print(f"Loading data from {data_path}")
        return pd.read_csv(data_path)
    print("Data file not found — generating synthetic data...")
    from generate_data import generate_disruption_data
    df = generate_disruption_data(6000)
    os.makedirs(os.path.dirname(data_path), exist_ok=True)
    df.to_csv(data_path, index=False)
    return df


def train(data_path: str = "data/disruption_data.csv",
          out_dir: str = "models/") -> None:
    os.makedirs(out_dir, exist_ok=True)

    # ── Load ───────────────────────────────────────────────────────────────────
    df = load_or_generate(data_path)
    X = df[FEATURES]
    y = df[TARGET]

    print(f"Dataset: {len(df)} rows")
    print("Label distribution:")
    for lbl, cnt in y.value_counts().sort_index().items():
        print(f"  {lbl} – {LABEL_NAMES[lbl]:<28} {cnt:>5} ({cnt/len(y)*100:.1f}%)")

    # ── Split ──────────────────────────────────────────────────────────────────
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, stratify=y, random_state=42
    )

    scaler = StandardScaler()
    X_train_s = scaler.fit_transform(X_train)
    X_test_s  = scaler.transform(X_test)

    # Compute class weights to handle imbalance
    class_counts = y_train.value_counts().to_dict()
    total = len(y_train)
    scale_pos = {cls: total / (len(class_counts) * cnt)
                 for cls, cnt in class_counts.items()}

    # ── Model ──────────────────────────────────────────────────────────────────
    model = XGBClassifier(
        n_estimators=400,
        max_depth=7,
        learning_rate=0.05,
        subsample=0.85,
        colsample_bytree=0.85,
        reg_alpha=0.1,
        reg_lambda=1.5,
        use_label_encoder=False,
        eval_metric="mlogloss",
        random_state=42,
        n_jobs=-1,
        num_class=5,
        objective="multi:softprob",
    )

    model.fit(
        X_train_s, y_train,
        eval_set=[(X_test_s, y_test)],
        verbose=False,
    )

    # ── Evaluation ────────────────────────────────────────────────────────────
    y_pred      = model.predict(X_test_s)
    y_pred_prob = model.predict_proba(X_test_s)

    acc = accuracy_score(y_test, y_pred)

    print(f"\n── Disruption Model Evaluation ───────────────────────")
    print(f"  Accuracy: {acc:.4f} ({acc*100:.2f}%)")
    print("\n  Classification Report:")
    print(classification_report(
        y_test, y_pred,
        target_names=[LABEL_NAMES[i] for i in range(5)],
        digits=3
    ))

    # CV
    cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
    cv_scores = cross_val_score(
        XGBClassifier(n_estimators=400, max_depth=7, learning_rate=0.05,
                      subsample=0.85, colsample_bytree=0.85,
                      eval_metric="mlogloss", random_state=42,
                      objective="multi:softprob", num_class=5),
        scaler.transform(X), y, cv=cv, scoring="accuracy", n_jobs=-1
    )
    print(f"  5-Fold CV Accuracy: {cv_scores.mean():.4f} ± {cv_scores.std():.4f}")

    # Feature importance
    importance = dict(zip(FEATURES, model.feature_importances_))
    top = sorted(importance.items(), key=lambda x: x[1], reverse=True)[:5]
    print("\n  Top-5 Feature Importances:")
    for feat, score in top:
        print(f"    {feat:<35} {score:.4f}")

    # ── Save artifacts ────────────────────────────────────────────────────────
    model_path  = os.path.join(out_dir, "disruption_model.pkl")
    scaler_path = os.path.join(out_dir, "disruption_scaler.pkl")
    meta_path   = os.path.join(out_dir, "disruption_meta.json")

    joblib.dump(model,  model_path)
    joblib.dump(scaler, scaler_path)

    meta = {
        "features": FEATURES,
        "target": TARGET,
        "label_names": LABEL_NAMES,
        "payout_multipliers": PAYOUT_MULTIPLIERS,
        "severity_scores": SEVERITY_SCORES,
        "metrics": {
            "accuracy": round(acc, 4),
            "cv_mean": round(cv_scores.mean(), 4),
            "cv_std": round(cv_scores.std(), 4),
        },
        "n_train": len(X_train),
        "n_test": len(X_test),
    }
    with open(meta_path, "w") as f:
        json.dump(meta, f, indent=2)

    print(f"\n  Saved → {model_path}")
    print(f"  Saved → {scaler_path}")
    print(f"  Saved → {meta_path}")
    print("\nDisruption model training complete ✓")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Train GigShield Disruption Classification Model")
    parser.add_argument("--data", default="data/disruption_data.csv")
    parser.add_argument("--out",  default="models/")
    args = parser.parse_args()
    train(args.data, args.out)
