"""
GigShield – Synthetic Data Generator
Generates training data for:
  1. XGBoost Premium Pricing model
  2. XGBoost Disruption Classification model
  3. Isolation Forest Fraud Detection model
"""

import numpy as np
import pandas as pd
from datetime import datetime, timedelta
import random
import os

np.random.seed(42)
random.seed(42)

# ─────────────────────────────────────────────
# 1. PREMIUM PRICING DATASET
# ─────────────────────────────────────────────
def generate_premium_data(n=5000):
    """
    Features that drive insurance premium:
      - rider_age           : age of the delivery partner
      - experience_months   : months active on platform
      - avg_daily_orders    : rolling 30-day average
      - city_tier           : 1 (metro), 2 (tier-2), 3 (tier-3)
      - vehicle_type        : 0=bicycle, 1=2-wheeler, 2=3-wheeler
      - historical_claims   : claims filed in last 12 months
      - avg_rainfall_mm     : average monthly rainfall in city
      - avg_aqi             : average AQI in rider's zone
      - coverage_amount     : desired weekly payout (₹)
      - plan_duration_weeks : 1, 4, or 12 weeks

    Target: weekly_premium (₹)
    """
    rows = []
    for _ in range(n):
        age = np.random.randint(18, 50)
        experience = np.random.randint(1, 72)
        avg_orders = np.random.uniform(5, 30)
        city_tier = np.random.choice([1, 2, 3], p=[0.5, 0.3, 0.2])
        vehicle = np.random.choice([0, 1, 2], p=[0.1, 0.8, 0.1])
        hist_claims = np.random.choice([0, 1, 2, 3], p=[0.6, 0.25, 0.1, 0.05])
        avg_rain = np.random.uniform(0, 300)
        avg_aqi = np.random.uniform(50, 400)
        coverage = np.random.choice([500, 750, 1000, 1500, 2000])
        duration = np.random.choice([1, 4, 12])

        # Actuarial-ish base pricing logic
        base = coverage * 0.03
        # Risk adjustments
        base += hist_claims * 4
        base += max(0, (avg_aqi - 150) * 0.02)
        base += max(0, (avg_rain - 100) * 0.01)
        base -= experience * 0.05          # experience discount
        base -= (duration - 1) * 0.5      # long-term discount
        base += (city_tier - 1) * 1.5     # tier-1 costlier
        base += (1 - vehicle) * 1.5        # bicycle riskier
        noise = np.random.normal(0, 1.5)
        premium = max(29, round(base + noise, 2))

        rows.append({
            "rider_age": age,
            "experience_months": experience,
            "avg_daily_orders": round(avg_orders, 2),
            "city_tier": city_tier,
            "vehicle_type": vehicle,
            "historical_claims": hist_claims,
            "avg_rainfall_mm": round(avg_rain, 2),
            "avg_aqi": round(avg_aqi, 1),
            "coverage_amount": coverage,
            "plan_duration_weeks": duration,
            "weekly_premium": premium,
        })

    return pd.DataFrame(rows)


# ─────────────────────────────────────────────
# 2. DISRUPTION CLASSIFICATION DATASET
# ─────────────────────────────────────────────
def generate_disruption_data(n=6000):
    """
    Parametric triggers evaluated in real-time:
      - rainfall_mm_3h      : rainfall in last 3 hours
      - wind_speed_kmh      : current wind speed
      - aqi_value           : current AQI reading
      - visibility_km       : current visibility
      - temp_celsius        : current temperature
      - civic_event_flag    : 0/1 (strike, protest, curfew)
      - hour_of_day         : 0–23
      - is_weekend          : 0/1
      - platform_order_drop : % drop in orders vs 7-day avg

    Target (multi-class):
      0 = No Disruption
      1 = Weather Disruption
      2 = Air Quality Disruption
      3 = Civic Disruption
      4 = Compound Disruption (2+ triggers)
    """
    rows = []
    for _ in range(n):
        rain = np.random.exponential(10)          # mostly low
        wind = np.random.uniform(0, 80)
        aqi = np.random.uniform(50, 500)
        visibility = np.random.uniform(0.2, 10)
        temp = np.random.uniform(10, 48)
        civic = np.random.choice([0, 1], p=[0.85, 0.15])
        hour = np.random.randint(0, 24)
        weekend = np.random.choice([0, 1], p=[0.7, 0.3])
        order_drop = np.random.uniform(-5, 60)

        # Determine label from thresholds
        weather_trigger = (rain > 35) or (wind > 50) or (visibility < 1.5)
        aqi_trigger = aqi > 250
        civic_trigger = civic == 1 or order_drop > 40

        active = sum([weather_trigger, aqi_trigger, civic_trigger])

        if active >= 2:
            label = 4
        elif weather_trigger:
            label = 1
        elif aqi_trigger:
            label = 2
        elif civic_trigger:
            label = 3
        else:
            label = 0

        # Add small label noise (real-world messiness)
        if np.random.random() < 0.03:
            label = np.random.randint(0, 5)

        rows.append({
            "rainfall_mm_3h": round(rain, 2),
            "wind_speed_kmh": round(wind, 2),
            "aqi_value": round(aqi, 1),
            "visibility_km": round(visibility, 2),
            "temp_celsius": round(temp, 1),
            "civic_event_flag": civic,
            "hour_of_day": hour,
            "is_weekend": weekend,
            "platform_order_drop_pct": round(order_drop, 2),
            "disruption_label": label,
        })

    return pd.DataFrame(rows)


# ─────────────────────────────────────────────
# 3. FRAUD DETECTION DATASET (for Isolation Forest)
# ─────────────────────────────────────────────
def generate_fraud_data(n=4000):
    """
    Claim-level features for anomaly detection:
      - claim_amount        : requested payout (₹)
      - time_since_purchase_hours : gap between policy buy & claim
      - disruption_severity_score : 0–1 score from disruption model
      - rider_claim_frequency_30d : claims in past 30 days
      - claims_in_zone_today : total claims from same geo-zone today
      - platform_orders_during_event : orders logged during event
      - account_age_days    : age of rider's account
      - policy_count_active : active policies at time of claim

    ~5% are injected fraud anomalies (for evaluation only — 
    Isolation Forest is unsupervised, no labels used in training).
    """
    rows = []
    for i in range(n):
        is_fraud = (i < int(n * 0.05))  # first 5% are fraud

        if is_fraud:
            # Anomalous patterns
            claim_amt = np.random.choice([
                np.random.uniform(1800, 2500),   # inflated
                np.random.uniform(10, 50),        # suspiciously low
            ])
            time_since = np.random.uniform(0, 2)         # instant claim
            severity = np.random.uniform(0, 0.2)         # low disruption
            claim_freq = np.random.randint(4, 15)        # high frequency
            zone_claims = np.random.randint(50, 200)     # zone spike
            orders_during = np.random.randint(8, 30)     # active during event
            acct_age = np.random.randint(1, 15)          # new account
            policy_count = np.random.randint(3, 8)       # multiple policies
        else:
            claim_amt = np.random.uniform(200, 1500)
            time_since = np.random.uniform(2, 72)
            severity = np.random.uniform(0.4, 1.0)
            claim_freq = np.random.choice([0, 1, 2], p=[0.7, 0.2, 0.1])
            zone_claims = np.random.randint(1, 30)
            orders_during = np.random.randint(0, 5)
            acct_age = np.random.randint(30, 1200)
            policy_count = np.random.choice([1, 2], p=[0.85, 0.15])

        rows.append({
            "claim_amount": round(claim_amt, 2),
            "time_since_purchase_hours": round(time_since, 2),
            "disruption_severity_score": round(severity, 4),
            "rider_claim_frequency_30d": claim_freq,
            "claims_in_zone_today": zone_claims,
            "platform_orders_during_event": orders_during,
            "account_age_days": acct_age,
            "policy_count_active": policy_count,
            "is_fraud_label": int(is_fraud),   # for eval only, NOT fed to IF
        })

    df = pd.DataFrame(rows)
    df = df.sample(frac=1, random_state=42).reset_index(drop=True)  # shuffle
    return df


# ─────────────────────────────────────────────
# ENTRYPOINT
# ─────────────────────────────────────────────
if __name__ == "__main__":
    os.makedirs("data", exist_ok=True)

    print("Generating premium pricing data...")
    df_premium = generate_premium_data(5000)
    df_premium.to_csv("data/premium_data.csv", index=False)
    print(f"  Saved {len(df_premium)} rows → data/premium_data.csv")

    print("Generating disruption classification data...")
    df_disruption = generate_disruption_data(6000)
    df_disruption.to_csv("data/disruption_data.csv", index=False)
    print(f"  Saved {len(df_disruption)} rows → data/disruption_data.csv")
    print(f"  Label distribution:\n{df_disruption['disruption_label'].value_counts().sort_index()}")

    print("Generating fraud detection data...")
    df_fraud = generate_fraud_data(4000)
    df_fraud.to_csv("data/fraud_data.csv", index=False)
    print(f"  Saved {len(df_fraud)} rows → data/fraud_data.csv")
    print(f"  Fraud label distribution:\n{df_fraud['is_fraud_label'].value_counts()}")

    print("\nAll datasets generated successfully.")
