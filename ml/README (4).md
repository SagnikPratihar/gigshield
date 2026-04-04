# GigShield ML Pipeline

AI/ML backend for parametric income insurance for food delivery partners.

## Architecture

```
Spring Boot (port 8080)
       │
       │ HTTP (internal)
       ▼
Flask ML API (port 5000)          Mock Sensors (port 5001)
  ├── /api/ml/premium             ├── /mock/weather/<city>
  ├── /api/ml/disruption          ├── /mock/aqi/<city>
  ├── /api/ml/fraud               ├── /mock/civic/<city>
  └── /api/ml/disruption/live     └── /mock/composite/<city>
```

## Models

| Model | Algorithm | Task | Key Metric |
|---|---|---|---|
| Premium Pricing | XGBoost Regressor | Predict weekly ₹ premium | MAE < ₹5 |
| Disruption Classifier | XGBoost Multi-class | Classify trigger type (0–4) | Accuracy > 92% |
| Fraud Detector | Isolation Forest | Flag anomalous claims | F1 > 0.80 |

### Disruption Labels
| Label | Type | Payout Multiplier |
|---|---|---|
| 0 | No Disruption | 0× |
| 1 | Weather Disruption | 1.0× |
| 2 | Air Quality Disruption | 0.75× |
| 3 | Civic Disruption | 0.85× |
| 4 | Compound Disruption | 1.5× |

## Quickstart

```bash
cd ml/

# Install dependencies
pip install -r requirements.txt

# 1. Generate data + train all models
python train_all.py

# 2. Start ML API
python app.py

# 3. (Optional) Start mock sensor APIs
python mock_sensors.py
```

## Individual training

```bash
python generate_data.py                    # generate all CSVs
python train_premium_model.py              # train premium model
python train_disruption_model.py           # train disruption model
python train_fraud_model.py                # train fraud model
```

## API Reference

### `POST /api/ml/premium`
```json
{
  "rider_age": 28,
  "experience_months": 18,
  "avg_daily_orders": 12.5,
  "city_tier": 1,
  "vehicle_type": 1,
  "historical_claims": 0,
  "avg_rainfall_mm": 120.0,
  "avg_aqi": 180.0,
  "coverage_amount": 1000,
  "plan_duration_weeks": 4
}
```
Response → `{ "weekly_premium": 87.43, "risk_band": "medium", ... }`

### `POST /api/ml/disruption`
```json
{
  "rainfall_mm_3h": 45.2,
  "wind_speed_kmh": 30.0,
  "aqi_value": 320.0,
  "visibility_km": 2.5,
  "temp_celsius": 32.0,
  "civic_event_flag": 0,
  "hour_of_day": 14,
  "is_weekend": 0,
  "platform_order_drop_pct": 15.0,
  "coverage_amount": 1000
}
```
Response → `{ "disruption_label": 2, "payout_triggered": true, "estimated_payout": 750.0, ... }`

### `POST /api/ml/fraud`
```json
{
  "claim_amount": 950.0,
  "time_since_purchase_hours": 18.5,
  "disruption_severity_score": 0.85,
  "rider_claim_frequency_30d": 1,
  "claims_in_zone_today": 12,
  "platform_orders_during_event": 1,
  "account_age_days": 240,
  "policy_count_active": 1
}
```
Response → `{ "fraud_flag": false, "risk_level": "low", "recommendation": "auto_approve", ... }`

### `GET /api/ml/disruption/live`
Returns live mock sensor readings classified by the disruption model.

### `GET /api/ml/health`
Returns model load status for all three models.

## File Structure

```
ml/
├── app.py                   # Flask ML API (port 5000)
├── mock_sensors.py          # Mock sensor APIs (port 5001)
├── generate_data.py         # Synthetic training data generator
├── train_premium_model.py   # XGBoost premium regressor
├── train_disruption_model.py# XGBoost disruption classifier
├── train_fraud_model.py     # Isolation Forest fraud detector
├── train_all.py             # Run full pipeline in one command
├── requirements.txt
├── data/                    # Generated CSVs (git-ignored)
│   ├── premium_data.csv
│   ├── disruption_data.csv
│   └── fraud_data.csv
└── models/                  # Saved .pkl + .json artifacts (git-ignored)
    ├── premium_model.pkl
    ├── premium_scaler.pkl
    ├── premium_meta.json
    ├── disruption_model.pkl
    ├── disruption_scaler.pkl
    ├── disruption_meta.json
    ├── fraud_model.pkl
    ├── fraud_scaler.pkl
    └── fraud_meta.json
```

## Environment Variables

| Variable | Default | Description |
|---|---|---|
| `MODELS_DIR` | `models/` | Path to saved model artifacts |
| `FLASK_PORT` | `5000` | Port for ML API |
| `FLASK_DEBUG` | `false` | Enable Flask debug mode |
| `MOCK_API_PORT` | `5001` | Port for mock sensors |
