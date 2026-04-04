"""
GigShield – Premium Pricing Model (XGBoost Regressor)
Predicts weekly insurance premium (₹) based on rider profile
and environmental risk factors.

Usage:
    python train_premium_model.py
    python train_premium_model.py --data data/premium_data.csv --out models/
"""

import argparse
import os
import json
import joblib
import numpy as np
import pandas as pd

from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from xgboost import XGBRegressor

# ─── Feature columns ───────────────────────────────────────────────────────────
FEATURES = [
    "rider_age",
    "experience_months",
    "avg_daily_orders",
    "city_tier",
    "vehicle_type",
    "historical_claims",
    "avg_rainfall_mm",
    "avg_aqi",
    "coverage_amount",
    "plan_duration_weeks",
]
TARGET = "weekly_premium"


def load_or_generate(data_path: str) -> pd.DataFrame:
    if os.path.exists(data_path):
        print(f"Loading data from {data_path}")
        return pd.read_csv(data_path)
    print("Data file not found — generating synthetic data...")
    from generate_data import generate_premium_data
    df = generate_premium_data(5000)
    os.makedirs(os.path.dirname(data_path), exist_ok=True)
    df.to_csv(data_path, index=False)
    return df


def train(data_path: str = "data/premium_data.csv",
          out_dir: str = "models/") -> None:
    os.makedirs(out_dir, exist_ok=True)

    # ── Load data ──────────────────────────────────────────────────────────────
    df = load_or_generate(data_path)
    X = df[FEATURES]
    y = df[TARGET]

    print(f"Dataset: {len(df)} rows | Target range: ₹{y.min():.2f} – ₹{y.max():.2f}")

    # ── Train/test split ───────────────────────────────────────────────────────
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # ── Scaler (for API consistency; XGBoost is scale-invariant but we expose it) ─
    scaler = StandardScaler()
    X_train_s = scaler.fit_transform(X_train)
    X_test_s  = scaler.transform(X_test)

    # ── Model ──────────────────────────────────────────────────────────────────
    model = XGBRegressor(
        n_estimators=300,
        max_depth=6,
        learning_rate=0.05,
        subsample=0.8,
        colsample_bytree=0.8,
        reg_alpha=0.1,
        reg_lambda=1.0,
        random_state=42,
        n_jobs=-1,
        eval_metric="rmse",
    )

    model.fit(
        X_train_s, y_train,
        eval_set=[(X_test_s, y_test)],
        verbose=False,
    )

    # ── Evaluation ────────────────────────────────────────────────────────────
    y_pred = model.predict(X_test_s)

    mae  = mean_absolute_error(y_test, y_pred)
    rmse = np.sqrt(mean_squared_error(y_test, y_pred))
    r2   = r2_score(y_test, y_pred)

    # 5-fold CV on training set
    cv_scores = cross_val_score(
        XGBRegressor(n_estimators=300, max_depth=6, learning_rate=0.05,
                     subsample=0.8, colsample_bytree=0.8, random_state=42),
        scaler.transform(X), y, cv=5, scoring="neg_mean_absolute_error", n_jobs=-1
    )
    cv_mae = -cv_scores.mean()

    print("\n── Premium Model Evaluation ──────────────────────────")
    print(f"  MAE  : ₹{mae:.2f}")
    print(f"  RMSE : ₹{rmse:.2f}")
    print(f"  R²   : {r2:.4f}")
    print(f"  CV MAE (5-fold): ₹{cv_mae:.2f}")

    # Feature importance
    importance = dict(zip(FEATURES, model.feature_importances_))
    top = sorted(importance.items(), key=lambda x: x[1], reverse=True)[:5]
    print("\n  Top-5 Feature Importances:")
    for feat, score in top:
        print(f"    {feat:<30} {score:.4f}")

    # ── Save artifacts ────────────────────────────────────────────────────────
    model_path  = os.path.join(out_dir, "premium_model.pkl")
    scaler_path = os.path.join(out_dir, "premium_scaler.pkl")
    meta_path   = os.path.join(out_dir, "premium_meta.json")

    joblib.dump(model,  model_path)
    joblib.dump(scaler, scaler_path)

    meta = {
        "features": FEATURES,
        "target": TARGET,
        "metrics": {"mae": round(mae, 4), "rmse": round(rmse, 4), "r2": round(r2, 4), "cv_mae": round(cv_mae, 4)},
        "n_train": len(X_train),
        "n_test": len(X_test),
        "model_params": model.get_params(),
    }
    with open(meta_path, "w") as f:
        json.dump(meta, f, indent=2, default=str)

    print(f"\n  Saved → {model_path}")
    print(f"  Saved → {scaler_path}")
    print(f"  Saved → {meta_path}")
    print("\nPremium model training complete ✓")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Train GigShield Premium Pricing Model")
    parser.add_argument("--data", default="data/premium_data.csv")
    parser.add_argument("--out",  default="models/")
    args = parser.parse_args()
    train(args.data, args.out)
