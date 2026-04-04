"""
GigShield – Fraud Detection Model (Isolation Forest)
Unsupervised anomaly detection on incoming claims.
Flags suspicious claims before payout is triggered.

Decision boundary:
  anomaly_score >= FRAUD_THRESHOLD → flag for manual review
  anomaly_score <  FRAUD_THRESHOLD → auto-approve

Usage:
    python train_fraud_model.py
    python train_fraud_model.py --data data/fraud_data.csv --out models/
"""

import argparse
import os
import json
import joblib
import numpy as np
import pandas as pd

from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import IsolationForest
from sklearn.metrics import precision_score, recall_score, f1_score, roc_auc_score

# ─── Constants ────────────────────────────────────────────────────────────────
FEATURES = [
    "claim_amount",
    "time_since_purchase_hours",
    "disruption_severity_score",
    "rider_claim_frequency_30d",
    "claims_in_zone_today",
    "platform_orders_during_event",
    "account_age_days",
    "policy_count_active",
]
LABEL_COL = "is_fraud_label"   # only used for evaluation, NOT training

# Isolation Forest outputs -1 (anomaly) or 1 (normal)
# We convert: -1 → fraud=1, 1 → fraud=0
FRAUD_THRESHOLD = 0.0           # decision_function score threshold
CONTAMINATION  = 0.05           # expected fraud rate (~5%)


def load_or_generate(data_path: str) -> pd.DataFrame:
    if os.path.exists(data_path):
        print(f"Loading data from {data_path}")
        return pd.read_csv(data_path)
    print("Data file not found — generating synthetic data...")
    from generate_data import generate_fraud_data
    df = generate_fraud_data(4000)
    os.makedirs(os.path.dirname(data_path), exist_ok=True)
    df.to_csv(data_path, index=False)
    return df


def train(data_path: str = "data/fraud_data.csv",
          out_dir: str = "models/") -> None:
    os.makedirs(out_dir, exist_ok=True)

    # ── Load ───────────────────────────────────────────────────────────────────
    df = load_or_generate(data_path)
    X_all = df[FEATURES]
    y_true = df[LABEL_COL]   # labels for eval only

    # Train ONLY on non-fraud rows (semi-supervised Isolation Forest approach)
    X_train = X_all[y_true == 0]
    print(f"Dataset: {len(df)} total | Training on {len(X_train)} normal samples")
    print(f"  Known fraud samples (for eval): {y_true.sum()}")

    # ── Scale ──────────────────────────────────────────────────────────────────
    scaler = StandardScaler()
    X_train_s = scaler.fit_transform(X_train)
    X_all_s   = scaler.transform(X_all)

    # ── Model ──────────────────────────────────────────────────────────────────
    model = IsolationForest(
        n_estimators=200,
        max_samples="auto",
        contamination=CONTAMINATION,
        max_features=1.0,
        bootstrap=False,
        random_state=42,
        n_jobs=-1,
    )
    model.fit(X_train_s)

    # ── Evaluation ────────────────────────────────────────────────────────────
    # IF predict: -1=anomaly(fraud), 1=normal
    y_pred_raw  = model.predict(X_all_s)
    y_pred      = (y_pred_raw == -1).astype(int)

    # Decision function scores (lower = more anomalous)
    scores = model.decision_function(X_all_s)

    # Evaluation against known labels
    prec  = precision_score(y_true, y_pred, zero_division=0)
    rec   = recall_score(y_true, y_pred, zero_division=0)
    f1    = f1_score(y_true, y_pred, zero_division=0)
    auc   = roc_auc_score(y_true, -scores)  # negate: lower score = higher fraud prob

    print("\n── Fraud Model Evaluation (unsupervised, labels for reference) ─────")
    print(f"  Precision : {prec:.4f}")
    print(f"  Recall    : {rec:.4f}")
    print(f"  F1-Score  : {f1:.4f}")
    print(f"  ROC-AUC   : {auc:.4f}")

    # Confusion matrix
    tp = int(((y_pred == 1) & (y_true == 1)).sum())
    fp = int(((y_pred == 1) & (y_true == 0)).sum())
    tn = int(((y_pred == 0) & (y_true == 0)).sum())
    fn = int(((y_pred == 0) & (y_true == 1)).sum())
    print(f"\n  Confusion Matrix:")
    print(f"    TP={tp}  FP={fp}")
    print(f"    FN={fn}  TN={tn}")

    # Score distribution
    fraud_scores  = scores[y_true == 1]
    normal_scores = scores[y_true == 0]
    print(f"\n  Anomaly Score Stats (lower = more suspicious):")
    print(f"    Fraud  → mean={fraud_scores.mean():.4f}  min={fraud_scores.min():.4f}  max={fraud_scores.max():.4f}")
    print(f"    Normal → mean={normal_scores.mean():.4f}  min={normal_scores.min():.4f}  max={normal_scores.max():.4f}")

    # ── Save artifacts ────────────────────────────────────────────────────────
    model_path  = os.path.join(out_dir, "fraud_model.pkl")
    scaler_path = os.path.join(out_dir, "fraud_scaler.pkl")
    meta_path   = os.path.join(out_dir, "fraud_meta.json")

    joblib.dump(model,  model_path)
    joblib.dump(scaler, scaler_path)

    meta = {
        "features": FEATURES,
        "contamination": CONTAMINATION,
        "fraud_threshold": FRAUD_THRESHOLD,
        "metrics": {
            "precision": round(prec, 4),
            "recall": round(rec, 4),
            "f1": round(f1, 4),
            "roc_auc": round(auc, 4),
        },
        "score_stats": {
            "fraud_mean": round(float(fraud_scores.mean()), 4),
            "normal_mean": round(float(normal_scores.mean()), 4),
        },
        "n_train": len(X_train),
        "n_eval": len(df),
    }
    with open(meta_path, "w") as f:
        json.dump(meta, f, indent=2)

    print(f"\n  Saved → {model_path}")
    print(f"  Saved → {scaler_path}")
    print(f"  Saved → {meta_path}")
    print("\nFraud detection model training complete ✓")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Train GigShield Fraud Detection Model")
    parser.add_argument("--data", default="data/fraud_data.csv")
    parser.add_argument("--out",  default="models/")
    args = parser.parse_args()
    train(args.data, args.out)
