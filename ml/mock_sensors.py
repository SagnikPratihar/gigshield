"""
GigShield – Mock Parametric Trigger APIs
Simulates real-world data sources for the demo:
  - Weather API (OpenWeatherMap mock)
  - AQI API (CPCB India mock)
  - Civic Disruption API (internal signal mock)

In production, replace these with real API calls.
Called by the disruption classification pipeline or Spring Boot directly.

Usage:
    python mock_sensors.py               # run as standalone Flask on port 5001
    from mock_sensors import get_weather, get_aqi, get_civic_signal  # import
"""

import os
import random
import math
from datetime import datetime
from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# ─── Deterministic-ish seeded randomness for reproducible demo ────────────────
def _seed_of_hour() -> int:
    """Returns a seed that changes every hour so demo readings feel 'live'."""
    now = datetime.now()
    return now.year * 1000000 + now.month * 10000 + now.day * 100 + now.hour


def get_weather(city: str = "Mumbai") -> dict:
    """Simulate OpenWeatherMap current-weather response."""
    random.seed(_seed_of_hour() + hash(city) % 1000)
    hour = datetime.now().hour

    # More rain at night/morning in monsoon season (Jun–Sep)
    month = datetime.now().month
    monsoon = month in [6, 7, 8, 9]
    base_rain = 40 if monsoon else 5

    rainfall = max(0, random.gauss(base_rain, 20))
    wind     = random.uniform(10, 70)
    vis      = max(0.3, 10 - rainfall * 0.08 + random.uniform(-1, 1))
    temp     = random.uniform(22, 44)

    return {
        "city": city,
        "rainfall_mm_3h": round(rainfall, 2),
        "wind_speed_kmh": round(wind, 2),
        "visibility_km":  round(vis, 2),
        "temp_celsius":   round(temp, 1),
        "humidity_pct":   round(random.uniform(40, 95), 1),
        "condition":      "rain" if rainfall > 20 else ("cloudy" if rainfall > 5 else "clear"),
        "source":         "mock_openweathermap",
        "timestamp":      datetime.utcnow().isoformat(),
    }


def get_aqi(city: str = "Delhi") -> dict:
    """Simulate CPCB India AQI API response."""
    random.seed(_seed_of_hour() + hash(city + "aqi") % 1000)
    hour = datetime.now().hour

    # Rush-hour AQI spike
    rush_bonus = 60 if (7 <= hour <= 10 or 17 <= hour <= 20) else 0
    aqi = max(30, random.gauss(180 + rush_bonus, 50))

    if aqi < 50:   category = "Good"
    elif aqi < 100: category = "Satisfactory"
    elif aqi < 200: category = "Moderate"
    elif aqi < 300: category = "Poor"
    elif aqi < 400: category = "Very Poor"
    else:           category = "Severe"

    return {
        "city": city,
        "aqi_value":     round(aqi, 1),
        "aqi_category":  category,
        "pm25_ugm3":     round(aqi * 0.4, 1),
        "pm10_ugm3":     round(aqi * 0.6, 1),
        "payout_trigger": aqi > 250,
        "source":        "mock_cpcb",
        "timestamp":     datetime.utcnow().isoformat(),
    }


def get_civic_signal(city: str = "Mumbai") -> dict:
    """Simulate internal civic disruption signal (strike/protest/curfew)."""
    random.seed(_seed_of_hour() + hash(city + "civic") % 1000)
    active = random.random() < 0.12   # ~12% chance of active event

    events = ["bandh", "protest", "curfew", "transport_strike", "heavy_traffic_advisory"]
    event_type = random.choice(events) if active else None

    # Platform order drop correlates with civic events
    if active:
        order_drop = random.uniform(30, 65)
    else:
        order_drop = random.uniform(-5, 20)

    return {
        "city": city,
        "civic_event_active": active,
        "civic_event_flag":   int(active),
        "event_type":         event_type,
        "platform_order_drop_pct": round(order_drop, 2),
        "severity":           "high" if active and order_drop > 50 else ("medium" if active else "none"),
        "payout_trigger":     active or order_drop > 40,
        "source":             "mock_internal_signals",
        "timestamp":          datetime.utcnow().isoformat(),
    }


def get_composite_reading(city: str = "Mumbai") -> dict:
    """Combined reading used by Flask ML API disruption/live endpoint."""
    weather = get_weather(city)
    aqi     = get_aqi(city)
    civic   = get_civic_signal(city)
    hour    = datetime.now().hour

    return {
        "city": city,
        "rainfall_mm_3h":           weather["rainfall_mm_3h"],
        "wind_speed_kmh":           weather["wind_speed_kmh"],
        "aqi_value":                aqi["aqi_value"],
        "visibility_km":            weather["visibility_km"],
        "temp_celsius":             weather["temp_celsius"],
        "civic_event_flag":         civic["civic_event_flag"],
        "hour_of_day":              hour,
        "is_weekend":               int(datetime.now().weekday() >= 5),
        "platform_order_drop_pct":  civic["platform_order_drop_pct"],
        # metadata
        "aqi_category":             aqi["aqi_category"],
        "event_type":               civic["event_type"],
        "timestamp":                datetime.utcnow().isoformat(),
    }


# ─── Endpoints (when run as standalone Flask app) ─────────────────────────────

@app.route("/mock/weather/<city>")
def weather_endpoint(city):
    return jsonify(get_weather(city))

@app.route("/mock/aqi/<city>")
def aqi_endpoint(city):
    return jsonify(get_aqi(city))

@app.route("/mock/civic/<city>")
def civic_endpoint(city):
    return jsonify(get_civic_signal(city))

@app.route("/mock/composite/<city>")
def composite_endpoint(city):
    return jsonify(get_composite_reading(city))

@app.route("/mock/health")
def health():
    return jsonify({"status": "ok", "timestamp": datetime.utcnow().isoformat()})


if __name__ == "__main__":
    port = int(os.environ.get("MOCK_API_PORT", 5001))
    print(f"Mock Sensor APIs running on port {port}")
    print(f"  GET /mock/weather/Mumbai")
    print(f"  GET /mock/aqi/Delhi")
    print(f"  GET /mock/civic/Bangalore")
    print(f"  GET /mock/composite/Mumbai")
    app.run(host="0.0.0.0", port=port, debug=False)
