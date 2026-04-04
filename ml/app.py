"""
GigShield – ML API (Flask)
Serves three model endpoints consumed by Spring Boot backend.

Endpoints:
  POST /api/ml/premium          → dynamic premium calculation
  POST /api/ml/disruption       → parametric trigger classification
  POST /api/ml/fraud            → claim fraud detection
  GET  /api/ml/health           → health check + model status
  GET  /api/ml/disruption/live  → evaluate current conditions (mock sensors)

Run:
  python app.py
  # or
  flask run --port 5000
"""

import os
import json
import joblib
import logging
import numpy as np
from datetime import datetime
from flask import Flask, request, jsonify
from flask_cors import CORS

# ─── Logging ──────────────────────────────────────────────────────────────────
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
logger = logging.getLogger(__name__)

app = Flask(__name__)
CORS(app)

# ─── Model registry ───────────────────────────────────────────────────────────
MODELS_DIR = os.environ.get("MODELS_DIR", "models/")

models = {}

def load_models():
    """Load all trained model artifacts at startup."""
    required = {
        "premium_model":     "premium_model.pkl",
        "premium_scaler":    "premium_scaler.pkl",
        "premium_meta":      "premium_meta.json",
        "disruption_model":  "disruption_model.pkl",
        "disruption_scaler": "disruption_scaler.pkl",
        "disruption_meta":   "disruption_meta.json",
        "fraud_model":       "fraud_model.pkl",
        "fraud_scaler":      "fraud_scaler.pkl",
        "fraud_meta":        "fraud_meta.json",
    }

    missing = []
    for key, filename in required.items():
        path = os.path.join(MODELS_DIR, filename)
        if not os.path.exists(path):
            missing.append(path)
            continue
        if filename.endswith(".json"):
            with open(path) as f:
                models[key] = json.load(f)
        else:
            models[key] = joblib.load(path)
        logger.info(f"Loaded: {path}")

    if missing:
        logger.warning(f"Missing model files (run train scripts first): {missing}")
    else:
        logger.info("All models loaded successfully ✓")


# ─── Helpers ──────────────────────────────────────────────────────────────────
def models_ready(*keys) -> bool:
    return all(k in models for k in keys)


def validate_fields(data: dict, required_fields: list) -> tuple:
    missing = [f for f in required_fields if f not in data]
    if missing:
        return False, f"Missing required fields: {missing}"
    return True, None


PAYOUT_MULTIPLIERS = {0: 0.0, 1: 1.0, 2: 0.75, 3: 0.85, 4: 1.5}
SEVERITY_SCORES    = {0: 0.0, 1: 0.85, 2: 0.70, 3: 0.75, 4: 1.0}
LABEL_NAMES = {
    0: "No Disruption",
    1: "Weather Disruption",
    2: "Air Quality Disruption",
    3: "Civic Disruption",
    4: "Compound Disruption",
}


# ─── Routes ───────────────────────────────────────────────────────────────────

@app.route("/api/ml/health", methods=["GET"])
def health():
    """Health check — returns model load status."""
    status = {
        "premium":    models_ready("premium_model", "premium_scaler"),
        "disruption": models_ready("disruption_model", "disruption_scaler"),
        "fraud":      models_ready("fraud_model", "fraud_scaler"),
    }
    all_ok = all(status.values())
    return jsonify({
        "status": "ok" if all_ok else "degraded",
        "models": status,
        "timestamp": datetime.utcnow().isoformat(),
    }), 200 if all_ok else 503


@app.route("/api/ml/premium", methods=["POST"])
def predict_premium():
    """
    Calculate dynamic weekly insurance premium.

    Request body (JSON):
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

    Response:
    {
        "weekly_premium": 87.43,
        "monthly_equivalent": 349.72,
        "risk_band": "medium",
        "breakdown": {...},
        "model_version": "xgb-v1"
    }
    """
    if not models_ready("premium_model", "premium_scaler"):
        return jsonify({"error": "Premium model not loaded. Run train_premium_model.py first."}), 503

    data = request.get_json(force=True)
    if not data:
        return jsonify({"error": "Request body must be JSON"}), 400

    REQUIRED = [
        "rider_age", "experience_months", "avg_daily_orders",
        "city_tier", "vehicle_type", "historical_claims",
        "avg_rainfall_mm", "avg_aqi", "coverage_amount", "plan_duration_weeks"
    ]
    ok, err = validate_fields(data, REQUIRED)
    if not ok:
        return jsonify({"error": err}), 400

    try:
        features = models["premium_meta"]["features"]
        X = np.array([[data[f] for f in features]])
        X_scaled = models["premium_scaler"].transform(X)

        raw_premium = float(models["premium_model"].predict(X_scaled)[0])
        weekly_premium = max(29.0, round(raw_premium, 2))

        # Risk band
        if weekly_premium < 50:
            risk_band = "low"
        elif weekly_premium < 100:
            risk_band = "medium"
        else:
            risk_band = "high"

        # Simple breakdown (approximate contribution per risk factor)
        hist_claims_impact = data["historical_claims"] * 4
        aqi_impact = max(0, (data["avg_aqi"] - 150) * 0.02)
        rain_impact = max(0, (data["avg_rainfall_mm"] - 100) * 0.01)
        experience_discount = data["experience_months"] * 0.05
        duration_discount = (data["plan_duration_weeks"] - 1) * 0.5
        base_rate = data["coverage_amount"] * 0.03

        return jsonify({
            "weekly_premium": weekly_premium,
            "monthly_equivalent": round(weekly_premium * 4, 2),
            "annual_equivalent": round(weekly_premium * 52, 2),
            "risk_band": risk_band,
            "breakdown": {
                "base_rate": round(base_rate, 2),
                "claims_loading": round(hist_claims_impact, 2),
                "aqi_loading": round(aqi_impact, 2),
                "rain_loading": round(rain_impact, 2),
                "experience_discount": round(experience_discount, 2),
                "long_term_discount": round(duration_discount, 2),
            },
            "coverage_amount": data["coverage_amount"],
            "model_version": "xgb-premium-v1",
            "timestamp": datetime.utcnow().isoformat(),
        }), 200

    except Exception as e:
        logger.error(f"Premium prediction error: {e}", exc_info=True)
        return jsonify({"error": str(e)}), 500


@app.route("/api/ml/disruption", methods=["POST"])
def classify_disruption():
    """
    Classify environmental conditions and determine payout trigger.

    Request body (JSON):
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
        "coverage_amount": 1000   (optional, for payout calc)
    }

    Response:
    {
        "disruption_label": 2,
        "disruption_type": "Air Quality Disruption",
        "payout_triggered": true,
        "payout_multiplier": 0.75,
        "estimated_payout": 750.0,
        "severity_score": 0.70,
        "confidence": 0.91,
        "probabilities": {...}
    }
    """
    if not models_ready("disruption_model", "disruption_scaler"):
        return jsonify({"error": "Disruption model not loaded. Run train_disruption_model.py first."}), 503

    data = request.get_json(force=True)
    if not data:
        return jsonify({"error": "Request body must be JSON"}), 400

    REQUIRED = [
        "rainfall_mm_3h", "wind_speed_kmh", "aqi_value",
        "visibility_km", "temp_celsius", "civic_event_flag",
        "hour_of_day", "is_weekend", "platform_order_drop_pct"
    ]
    ok, err = validate_fields(data, REQUIRED)
    if not ok:
        return jsonify({"error": err}), 400

    try:
        features = models["disruption_meta"]["features"]
        X = np.array([[data[f] for f in features]])
        X_scaled = models["disruption_scaler"].transform(X)

        label = int(models["disruption_model"].predict(X_scaled)[0])
        proba = models["disruption_model"].predict_proba(X_scaled)[0].tolist()
        confidence = float(max(proba))

        payout_multiplier = PAYOUT_MULTIPLIERS[label]
        severity_score    = SEVERITY_SCORES[label]
        payout_triggered  = label != 0

        coverage = data.get("coverage_amount", 0)
        estimated_payout = round(coverage * payout_multiplier, 2) if coverage else None

        return jsonify({
            "disruption_label": label,
            "disruption_type": LABEL_NAMES[label],
            "payout_triggered": payout_triggered,
            "payout_multiplier": payout_multiplier,
            "severity_score": severity_score,
            "confidence": round(confidence, 4),
            "estimated_payout": estimated_payout,
            "probabilities": {
                LABEL_NAMES[i]: round(p, 4) for i, p in enumerate(proba)
            },
            "model_version": "xgb-disruption-v1",
            "timestamp": datetime.utcnow().isoformat(),
        }), 200

    except Exception as e:
        logger.error(f"Disruption classification error: {e}", exc_info=True)
        return jsonify({"error": str(e)}), 500


@app.route("/api/ml/fraud", methods=["POST"])
def detect_fraud():
    """
    Evaluate an incoming claim for fraud signals.

    Request body (JSON):
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

    Response:
    {
        "fraud_flag": false,
        "anomaly_score": 0.123,
        "risk_level": "low",
        "recommendation": "auto_approve",
        "signals": [...]
    }
    """
    if not models_ready("fraud_model", "fraud_scaler"):
        return jsonify({"error": "Fraud model not loaded. Run train_fraud_model.py first."}), 503

    data = request.get_json(force=True)
    if not data:
        return jsonify({"error": "Request body must be JSON"}), 400

    REQUIRED = [
        "claim_amount", "time_since_purchase_hours", "disruption_severity_score",
        "rider_claim_frequency_30d", "claims_in_zone_today",
        "platform_orders_during_event", "account_age_days", "policy_count_active"
    ]
    ok, err = validate_fields(data, REQUIRED)
    if not ok:
        return jsonify({"error": err}), 400

    try:
        features = models["fraud_meta"]["features"]
        X = np.array([[data[f] for f in features]])
        X_scaled = models["fraud_scaler"].transform(X)

        prediction   = models["fraud_model"].predict(X_scaled)[0]    # -1 or 1
        raw_score    = float(models["fraud_model"].decision_function(X_scaled)[0])

        # Normalise score to 0–1 fraud probability (invert: lower raw = higher fraud)
        # Rough sigmoid normalisation
        fraud_prob = float(1 / (1 + np.exp(raw_score * 5)))
        fraud_flag = prediction == -1

        # Risk level
        if fraud_prob < 0.2:
            risk_level     = "low"
            recommendation = "auto_approve"
        elif fraud_prob < 0.5:
            risk_level     = "medium"
            recommendation = "soft_review"
        else:
            risk_level     = "high"
            recommendation = "manual_review"

        # Human-readable signals
        signals = []
        if data["time_since_purchase_hours"] < 2:
            signals.append("Claim filed within 2 hours of purchase")
        if data["rider_claim_frequency_30d"] >= 3:
            signals.append(f"High claim frequency: {data['rider_claim_frequency_30d']} in 30 days")
        if data["disruption_severity_score"] < 0.3 and data["claim_amount"] > 500:
            signals.append("Large claim amount with low disruption severity")
        if data["platform_orders_during_event"] > 5:
            signals.append(f"Rider completed {data['platform_orders_during_event']} orders during disruption event")
        if data["account_age_days"] < 30:
            signals.append("Account less than 30 days old")
        if data["policy_count_active"] >= 3:
            signals.append(f"Multiple active policies: {data['policy_count_active']}")
        if data["claims_in_zone_today"] > 40:
            signals.append(f"Zone spike: {data['claims_in_zone_today']} claims today in same zone")

        return jsonify({
            "fraud_flag": bool(fraud_flag),
            "fraud_probability": round(fraud_prob, 4),
            "anomaly_score": round(raw_score, 4),
            "risk_level": risk_level,
            "recommendation": recommendation,
            "signals": signals,
            "model_version": "iforest-fraud-v1",
            "timestamp": datetime.utcnow().isoformat(),
        }), 200

    except Exception as e:
        logger.error(f"Fraud detection error: {e}", exc_info=True)
        return jsonify({"error": str(e)}), 500


@app.route("/api/ml/disruption/live", methods=["GET"])
def live_disruption_check():
    """
    Evaluate current mock sensor readings and return live disruption status.
    In production this would pull from OpenWeatherMap / CPCB AQI APIs.
    For demo: returns randomised realistic readings.
    """
    import random
    from datetime import datetime

    hour = datetime.now().hour

    # Simulated live readings (replace with real API calls in production)
    mock_reading = {
        "rainfall_mm_3h":          round(random.uniform(0, 80), 2),
        "wind_speed_kmh":          round(random.uniform(5, 60), 2),
        "aqi_value":               round(random.uniform(80, 380), 1),
        "visibility_km":           round(random.uniform(0.5, 10), 2),
        "temp_celsius":            round(random.uniform(20, 42), 1),
        "civic_event_flag":        random.choice([0, 0, 0, 1]),
        "hour_of_day":             hour,
        "is_weekend":              int(datetime.now().weekday() >= 5),
        "platform_order_drop_pct": round(random.uniform(-5, 50), 2),
    }

    # Run through disruption model
    if not models_ready("disruption_model", "disruption_scaler"):
        return jsonify({
            "error": "Disruption model not loaded",
            "mock_reading": mock_reading
        }), 503

    try:
        features = models["disruption_meta"]["features"]
        X = np.array([[mock_reading[f] for f in features]])
        X_scaled = models["disruption_scaler"].transform(X)

        label = int(models["disruption_model"].predict(X_scaled)[0])
        proba = models["disruption_model"].predict_proba(X_scaled)[0].tolist()

        return jsonify({
            "live_readings": mock_reading,
            "disruption_label": label,
            "disruption_type": LABEL_NAMES[label],
            "payout_triggered": label != 0,
            "payout_multiplier": PAYOUT_MULTIPLIERS[label],
            "confidence": round(float(max(proba)), 4),
            "probabilities": {LABEL_NAMES[i]: round(p, 4) for i, p in enumerate(proba)},
            "data_source": "mock_sensors",
            "timestamp": datetime.utcnow().isoformat(),
        }), 200
    except Exception as e:
        return jsonify({"error": str(e), "mock_reading": mock_reading}), 500


# ─── Error handlers ───────────────────────────────────────────────────────────
@app.errorhandler(404)
def not_found(e):
    return jsonify({"error": "Endpoint not found", "available": [
        "GET  /api/ml/health",
        "POST /api/ml/premium",
        "POST /api/ml/disruption",
        "POST /api/ml/fraud",
        "GET  /api/ml/disruption/live",
    ]}), 404


@app.errorhandler(405)
def method_not_allowed(e):
    return jsonify({"error": "Method not allowed"}), 405


# ─── Main ─────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    load_models()
    port = int(os.environ.get("FLASK_PORT", 5000))
    debug = os.environ.get("FLASK_DEBUG", "false").lower() == "true"
    logger.info(f"Starting GigShield ML API on port {port} (debug={debug})")
    app.run(host="0.0.0.0", port=port, debug=debug)
