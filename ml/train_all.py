"""
GigShield – Train All Models
Runs the full ML pipeline in sequence:
  1. Generate synthetic training data
  2. Train premium pricing model (XGBoost)
  3. Train disruption classification model (XGBoost)
  4. Train fraud detection model (Isolation Forest)

Usage:
    python train_all.py
    python train_all.py --skip-data    (if data already generated)
    python train_all.py --models-dir custom_models/
"""

import argparse
import os
import time

import train_premium_model
import train_disruption_model
import train_fraud_model
from generate_data import (
    generate_premium_data,
    generate_disruption_data,
    generate_fraud_data,
)


def main():
    parser = argparse.ArgumentParser(description="GigShield – Full ML Pipeline")
    parser.add_argument("--skip-data",  action="store_true", help="Skip data generation")
    parser.add_argument("--data-dir",   default="data/",    help="Directory for CSV data files")
    parser.add_argument("--models-dir", default="models/",  help="Directory for saved model artifacts")
    args = parser.parse_args()

    os.makedirs(args.data_dir,   exist_ok=True)
    os.makedirs(args.models_dir, exist_ok=True)

    start_total = time.time()

    # ── Step 1: Data generation ────────────────────────────────────────────────
    if not args.skip_data:
        print("\n" + "═"*60)
        print("  STEP 1 — Generating Synthetic Training Data")
        print("═"*60)
        t0 = time.time()

        premium_path    = os.path.join(args.data_dir, "premium_data.csv")
        disruption_path = os.path.join(args.data_dir, "disruption_data.csv")
        fraud_path      = os.path.join(args.data_dir, "fraud_data.csv")

        df_p = generate_premium_data(5000)
        df_p.to_csv(premium_path, index=False)
        print(f"  ✓ Premium data    → {premium_path}  ({len(df_p)} rows)")

        df_d = generate_disruption_data(6000)
        df_d.to_csv(disruption_path, index=False)
        print(f"  ✓ Disruption data → {disruption_path}  ({len(df_d)} rows)")

        df_f = generate_fraud_data(4000)
        df_f.to_csv(fraud_path, index=False)
        print(f"  ✓ Fraud data      → {fraud_path}  ({len(df_f)} rows)")

        print(f"  Data generation time: {time.time()-t0:.1f}s")
    else:
        print("  Skipping data generation (--skip-data)")

    # ── Step 2: Premium model ─────────────────────────────────────────────────
    print("\n" + "═"*60)
    print("  STEP 2 — Training Premium Pricing Model (XGBoost Regressor)")
    print("═"*60)
    t0 = time.time()
    train_premium_model.train(
        data_path=os.path.join(args.data_dir, "premium_data.csv"),
        out_dir=args.models_dir,
    )
    print(f"  Training time: {time.time()-t0:.1f}s")

    # ── Step 3: Disruption model ───────────────────────────────────────────────
    print("\n" + "═"*60)
    print("  STEP 3 — Training Disruption Classifier (XGBoost Multi-class)")
    print("═"*60)
    t0 = time.time()
    train_disruption_model.train(
        data_path=os.path.join(args.data_dir, "disruption_data.csv"),
        out_dir=args.models_dir,
    )
    print(f"  Training time: {time.time()-t0:.1f}s")

    # ── Step 4: Fraud model ────────────────────────────────────────────────────
    print("\n" + "═"*60)
    print("  STEP 4 — Training Fraud Detector (Isolation Forest)")
    print("═"*60)
    t0 = time.time()
    train_fraud_model.train(
        data_path=os.path.join(args.data_dir, "fraud_data.csv"),
        out_dir=args.models_dir,
    )
    print(f"  Training time: {time.time()-t0:.1f}s")

    # ── Summary ───────────────────────────────────────────────────────────────
    elapsed = time.time() - start_total
    print("\n" + "═"*60)
    print(f"  ✅  All models trained in {elapsed:.1f}s")
    print(f"  Artifacts saved to: {os.path.abspath(args.models_dir)}/")
    print(f"    premium_model.pkl + premium_scaler.pkl + premium_meta.json")
    print(f"    disruption_model.pkl + disruption_scaler.pkl + disruption_meta.json")
    print(f"    fraud_model.pkl + fraud_scaler.pkl + fraud_meta.json")
    print("\n  Next step → python app.py  (starts Flask ML API on port 5000)")
    print("═"*60)


if __name__ == "__main__":
    main()
