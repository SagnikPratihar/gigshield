# 🛡️ GigShield
### AI-Powered Parametric Income Insurance for Food Delivery Partners

<div align="center">

![Guidewire DEVTrails 2026](https://img.shields.io/badge/Guidewire-DEVTrails%202026-orange?style=for-the-badge)
![Phase 2](https://img.shields.io/badge/Phase-1%20%7C%20Ideation%20%26%20Foundation-blue?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Active-green?style=for-the-badge)

> **"When the rain stops Rahul from delivering — GigShield pays him anyway."**

**An automated income safety net for Swiggy & Zomato delivery partners, triggered by real-world disruptions — zero paperwork, instant UPI payout.**

</div>

---

## 📌 Quick Navigation

| Section | What You'll Find |
|---------|-----------------|
| [🎯 The Problem](#-the-problem) | Why gig workers need this, right now |
| [💡 Our Solution](#-our-solution) | What GigShield does, in plain English |
| [👤 Who We're Building For](#-who-were-building-for) | Persona deep-dive with real scenarios |
| [🔄 How the App Works](#-how-the-app-works) | Full user journey, step by step |
| [💰 Weekly Premium Model](#-weekly-premium-model) | How pricing works — weekly, not annual |
| [⚡ Parametric Triggers](#-parametric-triggers) | What triggers a payout and why |
| [📱 Why Web, Not App](#-why-web-not-mobile-app) | Platform choice justification |
| [🤖 AI/ML Integration](#-aiml-integration) | Premium calc, fraud detection, forecasting |
| [🛠️ Tech Stack](#️-tech-stack) | What we're building with |
| [🏗️ Architecture](#️-system-architecture) | How all the pieces connect |
| [🗄️ Database Design](#️-database-design) | Schema overview |
| [📅 Development Plan](#-development-plan) | 6-week roadmap with milestones |
| [💹 Business Viability](#-business-viability) | Why this makes financial sense |
| [⚙️ Setup Guide](#️-setup--installation) | Get it running locally |
| [👥 Team](#-team) | Who we are |

---

## 🎯 The Problem

### India's Delivery Partners Have No Safety Net

Over **5 lakh food delivery partners** work daily for Swiggy and Zomato across India. They are independent contractors — no fixed salary, no sick leave, no employer protection.

Their income depends entirely on:
- How many hours they can physically work
- How many orders the platform sends their way
- Whether weather, roads, and civic conditions allow them to operate

### What Happens When Disruptions Strike?

When it rains heavily, when AQI spikes to dangerous levels, when a sudden curfew is called — **delivery stops**. Orders vanish. Restaurants stop dispatching. The worker simply sits and waits.

```
A typical Swiggy partner in Bangalore earns ₹800–₹1,000/day.
During a 3-hour monsoon downpour, they earn ₹0.
Across a monsoon month, they can lose ₹3,000–₹6,000 — 20–30% of their income.
Nobody compensates them. Not Swiggy. Not the government. Nobody.
```

### Why Nothing Else Works

| What Exists Today | Why It Doesn't Help |
|-------------------|---------------------|
| Swiggy/Zomato accident cover | Covers physical injuries only — not lost working hours |
| Health insurance (PMJJBY, PMSBY) | Life and accident only — zero income protection |
| Traditional general insurance | Annual premiums, complex claims, weeks to settle |
| Personal savings | Most delivery partners have no savings buffer |

**GigShield fills this exact gap — and nothing else does.**

> ⚠️ **Scope Boundary:** GigShield covers **income loss ONLY** caused by external disruptions. We strictly exclude health, life, accident medical bills, and vehicle repair coverage.

---

## 💡 Our Solution

**GigShield** is a parametric income insurance platform with three core ideas:

### Idea 1 — Parametric = No Claims Needed
In traditional insurance: you file a claim → investigator reviews it → weeks pass → maybe you get paid.

In GigShield: a disruption threshold is crossed → system validates automatically → money is in your UPI account within minutes. **No form. No call. No wait.**

### Idea 2 — Weekly Pricing = Built for Gig Workers
Gig workers think week to week. They get paid weekly. They plan weekly.
So GigShield charges **₹29–₹99 per week** — less than a coffee — renewable every Sunday. No annual commitment. Cancel or pause anytime.

### Idea 3 — AI Personalization = Pay What's Fair for Your Zone
A delivery partner in Coimbatore (rarely floods) should not pay the same premium as one in Mumbai's Dharavi zone during monsoon season.
GigShield's AI engine calculates a **personalized weekly premium** based on your actual zone's risk, the upcoming week's weather forecast, and your own activity history.

---

## 👤 Who We're Building For

### Primary Persona

| Attribute | Details |
|-----------|---------|
| **Name** | Rahul / Priya / Arjun |
| **Platform** | Swiggy or Zomato |
| **Age** | 19–38 years |
| **City** | Bangalore, Mumbai, Delhi, Chennai, Hyderabad, Pune |
| **Monthly Income** | ₹15,000–₹35,000 (highly variable) |
| **Weekly Earnings** | ₹3,500–₹8,000 |
| **Working Hours** | 8–14 hrs/day, 5–7 days/week |
| **Phone** | Android (budget to mid-range) |
| **Payments** | PhonePe / Google Pay / UPI |
| **Tech comfort** | Uses WhatsApp and delivery apps daily — comfortable with UPI |
| **Financial literacy** | Basic — understands simple transactions, unfamiliar with insurance terms |
| **Biggest fear** | A bad week wiping out rent money |

### What Rahul Needs From GigShield

```
✅ Understand it in under 2 minutes
✅ Pay less than ₹100/week
✅ Never file a claim manually
✅ Receive money within minutes of a disruption
✅ Trust that it actually works
```

---

## 🎬 Persona-Based Scenarios

These are real situations that happen every week across Indian cities.

---

### 📍 Scenario 1 — Monsoon Rainfall, Bangalore (July Peak)

> **Rahul**, Swiggy partner, Koramangala zone, Standard Shield (₹59/week)
>
> It's 7 PM Friday — the best earning hour of the week. Rain starts. Within 20 minutes, rainfall hits 42mm/hour. Restaurants stop dispatching. Rahul earns ₹0 for the next 2.5 hours.
>
> **What GigShield does:**
> OpenWeatherMap detects rainfall > 35mm/hr in Koramangala. Rahul's GPS confirms he's in zone. Platform mock API confirms he was active. Fraud score: 14/100. Payout: ₹280 (60% of 2.5-hr income). UPI transfer initiated. **Rahul gets ₹280 in 4 minutes.**

---

### 📍 Scenario 2 — Sudden Bandh, Mumbai (Monday Morning)

> **Priya**, Zomato partner, Andheri zone, Standard Shield
>
> 11 AM. A surprise local transport union strike is called. Roads blocked. Priya cannot reach any restaurant pickup point. Lunch shift completely lost.
>
> **What GigShield does:**
> Civic Alert API (mock) detects official restriction in Andheri. Priya's GPS is in the zone. Policy active. Payout: ₹420 (70% of 3-hr lunch shift income). **₹420 in her account in 6 minutes.**

---

### 📍 Scenario 3 — Severe AQI Spike, Delhi (November)

> **Vikram**, Swiggy partner, Lajpat Nagar zone, Pro Shield (₹99/week)
>
> Post-Diwali smog hits Delhi. AQI crosses 450 (Severe). Government issues outdoor advisory. Zomato volumes in the zone drop 65%. Vikram can barely breathe, let alone deliver.
>
> **What GigShield does:**
> CPCB AQI mock feed detects AQI > 400 in Vikram's zone. Active policy confirmed. Payout: ₹380 (50% of 4-hr income). **Auto-processed. No action needed from Vikram.**

---

### 📍 Scenario 4 — Extreme Heat, Hyderabad (May Afternoon)

> **Arjun**, Swiggy partner, Madhapur zone, Basic Shield (₹29/week)
>
> 2 PM. Temperature hits 46°C. IMD issues heat advisory. Outdoor work is dangerous. Order volumes collapse.
>
> **What GigShield does:**
> OpenWeatherMap detects 46°C in zone. Arjun's policy is active. Payout: ₹190 (50% of 2-hr income). **Credited instantly.**

---

### 📍 Scenario 5 — Flash Flood, Chennai (October)

> **Meena**, Zomato partner, T. Nagar zone, Pro Shield
>
> Overnight rain causes severe waterlogging in T. Nagar. Roads impassable for 4 hours during morning shift.
>
> **What GigShield does:**
> IMD flood alert (mock) flags T. Nagar zone. Meena's zone matches. Payout: ₹520 (80% of 4-hr income). **Money transferred before the water even recedes.**

---

## 🔄 How the App Works

### Worker Journey — From Signup to Payout

```
┌─────────────────────────────────────────────────────────────────┐
│  STEP 1 — SIGN UP  (< 3 minutes)                                │
│                                                                 │
│  Enter mobile number → Receive OTP → Verify                     │
│  Fill in: Name, City, Delivery Zone, Platform (Swiggy/Zomato)   │
│  Enter: Average daily working hours + UPI ID for payouts        │
│  Optionally link: Platform Partner ID (for activity validation) │
└────────────────────────────┬────────────────────────────────────┘
                             │
┌────────────────────────────▼────────────────────────────────────┐
│  STEP 2 — AI RISK PROFILING  (instant, automatic)               │
│                                                                 │
│  AI engine analyzes:                                            │
│   • Historical disruption frequency of your zone                │
│   • Upcoming 7-day weather forecast for your city               │
│   • Current season risk (monsoon, summer, etc.)                 │
│   • Your declared working hours                                 │
│                                                                 │
│  Output: Personalized weekly premium for each tier              │
└────────────────────────────┬────────────────────────────────────┘
                             │
┌────────────────────────────▼────────────────────────────────────┐
│  STEP 3 — CHOOSE A PLAN & PAY                                   │
│                                                                 │
│  See 3 plans with your personalized price                       │
│  Pick a plan → Pay via UPI (Razorpay test mode)                 │
│  Policy is ACTIVE immediately                                   │
└────────────────────────────┬────────────────────────────────────┘
                             │
┌────────────────────────────▼────────────────────────────────────┐
│  STEP 4 — COVERAGE RUNS IN THE BACKGROUND                       │
│                                                                 │
│  Spring Boot scheduler polls weather + civic APIs every 15 min  │
│  Worker sees "✅ Covered This Week" on their home screen        │
│  Worker goes about their day normally — no action needed        │
└────────────────────────────┬────────────────────────────────────┘
                             │
                   ┌─────────▼──────────┐
                   │  Disruption Found? │
                   └─────────┬──────────┘
                      YES    │     NO
           ┌────────────────┘     └──────────────────┐
           ▼                                          ▼
┌──────────────────────────┐             ┌────────────────────────┐
│  STEP 5 — VALIDATE       │             │  Keep monitoring       │
│                          │             │  Next check in 15 min  │
│  ✓ Worker in affected    │             └────────────────────────┘
│    zone? (GPS check)     │
│  ✓ Policy active?        │
│  ✓ Worker was working    │
│    at that time?         │
│  ✓ Not a duplicate       │
│    claim for same event? │
└──────────┬───────────────┘
           │ ALL PASS
┌──────────▼───────────────┐
│  STEP 6 — FRAUD CHECK    │
│                          │
│  ML model scores claim   │
│  0–100 risk score        │
└──────────┬───────────────┘
           │
    ┌──────┴──────────────┐
    ▼                     ▼
Score < 70            Score ≥ 70
    │                     │
    ▼                     ▼
AUTO-APPROVE          FLAG FOR ADMIN
    │                 REVIEW (24 hrs)
    ▼
┌──────────────────────────┐
│  STEP 7 — INSTANT PAYOUT │
│                          │
│  Calculate payout amount │
│  Initiate UPI transfer   │
│  SMS + App notification  │
│  "₹280 credited! 🎉"    │
└──────────────────────────┘
           │
┌──────────▼───────────────────────────────────────────────────┐
│  STEP 8 — WEEKLY RENEWAL (Every Sunday Midnight)             │
│                                                              │
│  Friday evening: "Your new premium for next week is ₹52"     │
│  Worker can: Renew / Upgrade / Downgrade / Pause             │
│  Auto-renewal is ON by default (worker can turn it off)      │
└──────────────────────────────────────────────────────────────┘
```


### Admin Dashboard

> **Planned for Phase 3 (April 5–17)**
> The admin panel is not part of the current development scope.
> It will be built in the final phase once the core worker-facing
> platform and automated payout engine are stable.

### Planned Features

| Feature | Description |
|---------|-------------|
| Live Disruption Feed | Real-time view of active trigger events across all zones |
| Claims Review Queue | Manual review for claims flagged by fraud detection (score ≥ 70) |
| Fraud Alerts Panel | GPS anomalies, duplicate claims, high-risk workers flagged |
| Loss Ratio Tracker | Premiums collected vs payouts made — per zone, per week |
| Payout Audit Log | Full searchable record of every payout (who, why, when, where) |
| 7-Day Risk Forecast | Predicted disruption probability and payout liability per zone |
| Worker Analytics | Active policies, churn rate, zone-wise coverage distribution |


---

## 💰 Weekly Premium Model

### Why Weekly?

Gig workers receive platform payouts **weekly**. They plan expenses **weekly**. Annual insurance requires a large upfront sum that most delivery partners simply don't have.

GigShield charges weekly — as low as **₹29/week** — debited from the same account where they receive their Swiggy/Zomato earnings. It feels like a small, automatic deduction, not a financial burden.

---

### The Three Plans

| Plan | Weekly Cost | Max Daily Payout | Max Weekly Payout | Best For |
|------|------------|-----------------|------------------|----|
| 🟢 **Basic Shield** | ₹29/week | ₹250/day | ₹500/week | Part-timers, 4–6 hrs/day |
| 🔵 **Standard Shield** | ₹59/week | ₹500/day | ₹1,200/week | Full-timers, 8–10 hrs/day |
| 🟣 **Pro Shield** | ₹99/week | ₹900/day | ₹2,500/week | Power workers, 12+ hrs, high-risk zones |

> These are **base prices**. The AI engine adjusts them each week based on your specific risk.

---

### How AI Adjusts Your Premium Each Week

The base price goes **up or down** based on 8 real-world signals:

| Signal | How It Affects Your Price |
|--------|--------------------------|
| Your zone's historical flood/rain incidents | Flood-prone zone → price goes up |
| 7-day weather forecast for your area | Heavy rain predicted → price goes up |
| City + season risk (e.g., Mumbai in July) | Peak monsoon → multiplier applied |
| Your average daily working hours | More hours = more exposure = slight increase |
| AQI trend in your zone | Pollution-heavy week → price goes up |
| Civic risk index (protest/strike history) | High-risk area → slight increase |
| Your personal claim legitimacy history | Clean history → price goes down |
| Zone's overall risk tier (1–5) | Lower tier = lower price |

**Adjustment range: ±30% of base price**

---

### Real Pricing Examples

```
Example A — LOW RISK
Rahul | Bangalore | Whitefield zone | Standard Shield (base ₹59)
Week: Non-monsoon | Clear forecast | Historically safe zone | No past claims
AI adjustment: −₹14
→ Rahul pays ₹45 this week ✅

Example B — HIGH RISK
Priya | Mumbai | Dharavi zone | Standard Shield (base ₹59)
Week: Peak monsoon | 4-day heavy rain forecast | Flood-prone zone
AI adjustment: +₹23
→ Priya pays ₹82 this week ✅
```

---

### How Payout Amounts Are Calculated

```
Payout = Average Hourly Income × Disruption Hours × Trigger Payout % 
         (capped at daily/weekly limit of chosen plan)

Where:
  Average Hourly Income = Declared weekly earnings ÷ Declared weekly hours
  Disruption Hours      = How long the trigger was active in your zone
  Trigger Payout %      = Fixed per trigger type (50%–80%) — see triggers table
```

**Example:**
> Rahul earns ₹700/day working 7 hours → ₹100/hour
> Heavy rain lasts 2.5 hours in his zone
> Payout % for rain = 60%
> **Payout = ₹100 × 2.5 × 60% = ₹150** (within ₹500 daily cap) ✅

---

### Renewal Flow

```
Every Friday 6 PM  →  Notification: "Your coverage renews Sunday. New premium: ₹52"
                       Worker can change plan or pause — they have until Sunday 11:59 PM

Every Sunday midnight  →  Auto-renewal triggers
                           Payment via saved UPI
                           New week's coverage begins immediately

If payment fails  →  2-hour grace period, then coverage pauses (no payouts during gap)
```

---

## ⚡ Parametric Triggers

### What Makes a Good Trigger?

A parametric trigger must be:
- **Objective** — measured by third-party data, not worker's word
- **Location-specific** — happening in the worker's actual delivery zone
- **Time-matched** — occurring during the worker's active work hours
- **Verifiable** — from a trusted public/government API source

### The 5 Triggers We've Designed

---

#### 🌧️ Trigger 1 — Heavy Rainfall

| | |
|---|---|
| **Data Source** | OpenWeatherMap API (real, free tier) |
| **Threshold** | > 35mm/hour sustained for 30+ minutes in worker's zone |
| **Coverage Cities** | Bangalore, Mumbai, Chennai, Hyderabad, Kolkata, Delhi, Pune |
| **Payout Rate** | **60%** of average hourly income per disruption hour |
| **Validation** | Worker's GPS within 3km of zone centroid during event |
| **Max Payout Hours** | 6 hours per event |
| **Why This Threshold?** | 35mm/hr = "heavy rain" classification by IMD. At this level, restaurant dispatching visibly slows. |

---

#### 🌊 Trigger 2 — Flood / Waterlogging

| | |
|---|---|
| **Data Source** | IMD Flood Advisory API (mocked JSON in Phase 1–2) |
| **Threshold** | Official zone-level waterlogging/flood advisory issued |
| **Coverage Cities** | Mumbai, Chennai, Kolkata, Bhubaneswar, Patna |
| **Payout Rate** | **80%** of average hourly income per disruption hour |
| **Validation** | Worker's zone matches advisory zone + policy active |
| **Max Payout Hours** | 8 hours per event |

---

#### ☀️ Trigger 3 — Extreme Heat

| | |
|---|---|
| **Data Source** | OpenWeatherMap API (real, free tier) |
| **Threshold** | > 45°C sustained for 2+ consecutive hours in zone |
| **Coverage Cities** | Delhi, Hyderabad, Nagpur, Lucknow, Jaipur, Agra |
| **Payout Rate** | **50%** of average hourly income per disruption hour |
| **Validation** | Worker zone temperature match + active hours overlap |
| **Max Payout Hours** | 5 hours per event |

---

#### 😷 Trigger 4 — Severe Air Pollution (AQI)

| | |
|---|---|
| **Data Source** | CPCB AQI API (mocked; real CPCB data available via data.gov.in) |
| **Threshold** | AQI > 400 (Severe category) in worker's city zone |
| **Coverage Cities** | Delhi, Noida, Gurugram, Mumbai, Kolkata |
| **Payout Rate** | **50%** of average hourly income per disruption hour |
| **Validation** | City-level AQI match + worker zone confirmed |
| **Max Payout Hours** | 8 hours per event |

---

#### 🚧 Trigger 5 — Civic Disruption (Curfew / Bandh / Strike)

| | |
|---|---|
| **Data Source** | Civic Alert API (mocked JSON — simulates official advisories) |
| **Threshold** | Official government or civic body restriction issued for worker's zone |
| **Coverage Cities** | All covered cities |
| **Payout Rate** | **70%** of average hourly income per disruption hour |
| **Validation** | Official alert source + zone match + worker GPS in zone |
| **Max Payout Hours** | 10 hours per event |

---

### Trigger Monitoring — How It Works Behind the Scenes

```
Every 15 minutes, Spring Boot Scheduler runs:

  ┌── Poll OpenWeatherMap → Rainfall + Temperature for all active zones
  ├── Poll CPCB AQI mock  → AQI levels for active zones
  ├── Poll IMD Flood mock → Any zone-level flood advisories
  └── Poll Civic API mock → Any curfew or strike alerts

  For every threshold breach found:
    │
    ├── Find all workers with active policies in that zone
    └── For each worker:
          ✓ GPS in zone?
          ✓ Policy active?
          ✓ Working hours overlap?
          ✓ Not already claimed for this event?
          → Run fraud check
          → Auto-payout or flag for review
```

---

## 📱 Why Web, Not Mobile App?

We chose a **mobile-responsive React web app** over a native Android/iOS application.

| Criterion | Native App | Our Choice: Web App |
|-----------|-----------|----------------------|
| Install friction | High — Play Store download required | ✅ Zero — open via link in browser |
| Sharing / reach | App store discovery only | ✅ WhatsApp link, QR code, SMS |
| Update speed | 2–5 days (store review) | ✅ Instant server push |
| Development cost | High — separate iOS + Android | ✅ Single React codebase |
| UPI payment | Supported | ✅ Supported via browser |
| "App feel" | Native | ✅ PWA "Add to Home Screen" |
| Works on low-end Android | Variable | ✅ Browser-based, lightweight |

**Key Insight:** Delivery partners already receive platform communication via **WhatsApp links** and **SMS**. A link they can tap and open instantly — with no download — is far more accessible than an app. The web app can be pinned to their home screen via PWA, giving a near-native experience.

---

## 🤖 AI/ML Integration

We integrate AI/ML into **three distinct parts** of the product workflow:

---

### Module 1 — Dynamic Weekly Premium Calculator

**Where it fits:** After onboarding, and every Friday before renewal.

**What problem it solves:** Without personalized pricing, we'd either overcharge workers in safe zones (they'd leave) or undercharge workers in high-risk zones (we'd lose money). AI pricing makes it fair for everyone.

**How it works:**

```
INPUT FEATURES (per worker, per week):
├── Zone ID (encoded to historical risk score)
├── City risk tier (1 = very safe → 5 = very high risk)
├── Season/month (cyclically encoded — captures monsoon seasonality)
├── 7-day rainfall forecast (mm) from OpenWeatherMap
├── 7-day max temperature forecast (°C)
├── Zone's historical flood events (last 12 months)
├── Zone's historical rain-above-threshold events (last 12 months)
├── Worker's declared average daily working hours
├── Worker's claim legitimacy score (0–1, from history)
├── Zone's 7-day average AQI
└── Zone's civic risk index (0–1)

MODEL: Gradient Boosting Regressor (XGBoost)

OUTPUT: ± ₹ adjustment to apply to the worker's base tier price
```

**Deployment Roadmap:**

| Phase | Approach |
|-------|---------|
| Phase 1 (now) | Rule-based weighted scoring — no ML library needed, simulates model output |
| Phase 2 | Real XGBoost model, exported from Python, served as REST API from Spring Boot |
| Phase 3 | Weekly automated retraining pipeline using accumulated claims + weather data |

---

### Module 2 — Intelligent Fraud Detection Engine

**Where it fits:** Every time a payout is auto-triggered.

**What problem it solves:** Parametric insurance without fraud protection is an open door for abuse — fake GPS locations, claims during non-working hours, duplicate submissions. We catch all of these.

**Fraud Types We Detect:**

| Fraud Type | How It Happens | How We Catch It |
|-----------|----------------|-----------------|
| **GPS Spoofing** | Worker uses a fake GPS app to pretend they're in the disruption zone | Trajectory analysis — impossible speed between GPS points, device fingerprint check |
| **Fake Active Hours** | Claims disruption during hours they weren't working | Cross-reference with platform activity API (simulated) |
| **Duplicate Claims** | Submitting the same event twice | Event ID + Worker ID deduplication in database |
| **Zone Misrepresentation** | Registered in a high-risk zone, actually works elsewhere | GPS history vs registered zone comparison over time |
| **Claim Clusters** | Many workers from same area filing within seconds | Anomaly detection on claim burst patterns |
| **Synthetic Profiles** | Fake worker accounts created for payouts | OTP verification, platform Partner ID validation |

**Fraud Scoring Model: Isolation Forest (Anomaly Detection)**

```
INPUT FEATURES:
├── Worker GPS (lat/lng at time of event)
├── Disruption zone center coordinates
├── Distance: worker to zone (km)
├── Worker's platform activity status (active/inactive)
├── Claim frequency in last 30 days
├── Average claim amount in last 30 days
├── Hours since last claim
├── Device ID match (same device as registration?)
├── GPS trajectory anomaly score
└── Number of other workers claiming same event

OUTPUT: Fraud Risk Score (0–100)
  0–30:   Auto-approve immediately
  31–69:  Auto-approve + flag for admin to review later
  70–100: Hold payout → send to admin review queue (resolved within 24 hrs)
```

**Hard Rules (Always checked first — instant reject if any fail):**
```
✗ Worker GPS > 5km from disruption zone → REJECT
✗ Duplicate claim: same event + same worker → REJECT
✗ Worker platform status = Inactive during event → FLAG
✗ Claim filed > 2 hours after event ended → FLAG
```

---

### Module 3 — Predictive Risk Dashboard (Admin)

**Where it fits:** Admin/insurer view, updated daily.

**What problem it solves:** Insurers need to know how much money to reserve for next week's payouts before claims arrive. Surprises are bad for business.

**What it predicts:**

```
For each city zone, for the next 7 days:
├── Probability of a triggerable disruption (0–100%)
├── Expected number of claims
├── Estimated total payout liability
└── Recommended reserve amount
```

**Model:** Time-series forecasting using weather history + seasonal patterns
- **Phase 1–2:** Static mock forecast data shown in admin dashboard (looks real, hardcoded)
- **Phase 3:** Live forecasting model using Prophet/ARIMA integrated with real data

---

## 🛠️ Tech Stack

### Why This Stack?

We chose tools that are **industry-standard, well-documented, and fast to build with** — maximizing output in a 6-week competition.

### Frontend

| Technology | Version | Why We Chose It |
|-----------|---------|----------------|
| **React** | 18.x | Most popular frontend framework, component-based, great ecosystem |
| **Tailwind CSS** | 3.x | Utility-first — builds mobile-responsive UIs fast without custom CSS |
| **React Router** | v6 | Clean client-side navigation |
| **Axios** | 1.x | Simple, reliable HTTP calls to Spring Boot |
| **Recharts** | 2.x | Beautiful charts for admin analytics dashboard **(Future Update)**|
| **React Hook Form** | 7.x | Fast, lightweight form handling for onboarding |
| **Zustand** | 4.x | Minimal global state (auth context, user session) |
| **React Hot Toast** | 2.x | Push notifications for payout alerts and policy confirmations |
| **Vite** | 5.x | Faster build tool than CRA — instant hot-reload in dev |

### Backend

| Technology | Version | Why We Chose It |
|-----------|---------|----------------|
| **Spring Boot** | 3.2.x | Industry-standard Java framework — REST APIs, security, scheduling built in |
| **Spring Security + JWT** | 6.x / 0.12.x | Stateless auth — scales easily, no session storage needed |
| **Spring Data JPA** | 3.2.x | Eliminates boilerplate SQL — entity-to-table mapping done simply |
| **Spring Scheduler** | Built-in | Runs disruption monitor every 15 min and weekly renewal at midnight |
| **OpenFeign** | Spring Cloud | Clean HTTP client for calling weather and mock APIs |
| **Lombok** | 1.18.x | Removes getter/setter boilerplate — cleaner code |
| **MapStruct** | 1.5.x | Auto-maps DTOs to entities — prevents leaking DB models to API |
| **Flyway** | 9.x | Version-controlled DB migrations — team can't break each other's schema |
| **Maven** | 3.9.x | Standard Java build tool |
| **Java** | 17 LTS | Stable, long-term support version |

### Database

| Technology | Version | Why We Chose It |
|-----------|---------|----------------|
| **MySQL** | 8.0.x | Reliable relational DB — well suited for transactional insurance data |
| **HikariCP** | Built-in | Fastest Java connection pool — handles concurrent API calls efficiently |

### External Integrations

| Integration | Type | Used For |
|------------|------|---------|
| **OpenWeatherMap API** | Real (free tier) | Live rainfall and temperature per zone |
| **CPCB AQI Feed** | Mocked JSON | Air quality index monitoring |
| **IMD Flood Advisory** | Mocked JSON | Flood/waterlogging alerts |
| **Civic Alert Feed** | Mocked JSON | Curfew, bandh, strike notifications |
| **Razorpay** | Test/Sandbox mode | Simulated UPI payouts to workers |
| **Platform Activity API** | Simulated mock | Validate worker was active during disruption |

---

## 🏗️ System Architecture

```
┌─────────────────────────────────────────────────────────────────────┐
│                           CLIENT LAYER                              │
│                                                                     │
│     ┌──────────────────────────┐      ┌──────────────────────────┐  │
│     │    WORKER APP (React)    │      │   ADMIN PANEL (React)    │  │
│     │  • Onboarding            │      │  • Live disruption feed  │  │
│     │  • Plan selection        │      │  • Claims review queue   │  │
│     │  • Coverage status       │      │  • Fraud alerts          │  │
│     │  • Payout tracker        │      │  • Analytics dashboard   │  │
│     └────────────┬─────────────┘      └─────────────┬────────────┘  │
└──────────────────┼──────────────────────────────────┼───────────────┘
                   │  HTTPS / REST / JSON             │
┌──────────────────▼──────────────────────────────────▼───────────────┐
│                   SPRING BOOT APPLICATION (Port 8080)               │
│                                                                     │
│  ┌──────────────┐  ┌──────────────┐  ┌─────────────────────────┐    │
│  │ Auth Service │  │ User/Profile │  │    Policy Service       │    │
│  │ (JWT + OTP)  │  │   Service    │  │ (create, renew, cancel) │    │
│  └──────────────┘  └──────────────┘  └─────────────────────────┘    │
│                                                                     │
│  ┌──────────────┐  ┌──────────────┐  ┌─────────────────────────┐    │
│  │   Premium    │  │  Claims +    │  │    Payout Service       │    │
│  │  Calculator  │  │  Fraud Svc   │  │   (Razorpay sandbox)    │    │
│  │  (AI Model)  │  │  (ML Score)  │  │                         │    │
│  └──────────────┘  └──────────────┘  └─────────────────────────┘    │
│                                                                     │
│  ┌────────────────────────────────────────────────────────────────┐ │
│  │               DISRUPTION MONITOR (Spring Scheduler)            │ │
│  │   Runs every 15 minutes → checks all 5 trigger APIs            │ │
│  │   Fires auto-claims → runs fraud check → initiates payouts     │ │
│  └────────────────────────────────────────────────────────────────┘ │
└───────────────────────────────┬──────────────────────────────────────┘
                                │
            ┌───────────────────┼──────────────────────┐
            ▼                   ▼                       ▼
  ┌──────────────────┐  ┌────────────────────┐  ┌──────────────────┐
  │   MySQL 8.0      │  │  External APIs     │  │  AI/ML Module    │
  │                  │  │                    │  │                  │
  │  users           │  │  OpenWeatherMap ✅ │  │  Premium Calc   │
  │  zones           │  │  CPCB AQI (mock)   │  │  Fraud Scorer    │
  │  policies        │  │  IMD Flood (mock)  │  │  Risk Forecast   │
  │  disruptions     │  │  Civic API (mock)  │  │                  │
  │  claims          │  │  Razorpay test ✅  │  │  (REST endpoint  │
  │  payouts         │  │  Platform (mock)   │  │   from Python)   │
  │  fraud_logs      │  └────────────────────┘  └──────────────────┘
  │  premium_log     │
  └──────────────────┘
```

---

## 🗄️ Database Design

### Table Overview

| Table | What It Stores |
|-------|---------------|
| `users` | Worker profiles — name, city, zone, UPI ID, platform |
| `zones` | Delivery zones per city — coordinates, risk tier, flood-prone flag |
| `policies` | Weekly insurance policies — tier, premium, coverage dates, status |
| `disruption_events` | Verified disruption events — type, zone, threshold value, duration |
| `claims` | Auto-generated claims — payout amount, fraud score, status |
| `payouts` | UPI transfer records — Razorpay TXN ID, status, timestamps |
| `premium_calculations` | Audit log of every AI premium decision — inputs + output |
| `fraud_logs` | Every fraud check — scores, GPS data, flags triggered |
| `admins` | Admin user accounts with roles |

### Key Schema Snippets

```sql
-- Core worker table
CREATE TABLE users (
    id                  BIGINT AUTO_INCREMENT PRIMARY KEY,
    mobile_number       VARCHAR(15) UNIQUE NOT NULL,
    full_name           VARCHAR(100) NOT NULL,
    city                VARCHAR(50) NOT NULL,
    zone_id             BIGINT NOT NULL,
    platform            ENUM('SWIGGY', 'ZOMATO') NOT NULL,
    platform_partner_id VARCHAR(50),               -- for activity validation
    upi_id              VARCHAR(100) NOT NULL,
    avg_daily_hours     DECIMAL(4,2),
    avg_hourly_income   DECIMAL(10,2),
    is_active           BOOLEAN DEFAULT TRUE,
    created_at          TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (zone_id) REFERENCES zones(id)
);

-- Weekly policies
CREATE TABLE policies (
    id                BIGINT AUTO_INCREMENT PRIMARY KEY,
    worker_id         BIGINT NOT NULL,
    tier              ENUM('BASIC', 'STANDARD', 'PRO') NOT NULL,
    base_premium      DECIMAL(10,2) NOT NULL,
    actual_premium    DECIMAL(10,2) NOT NULL,       -- AI-adjusted price
    max_daily_payout  DECIMAL(10,2) NOT NULL,
    max_weekly_payout DECIMAL(10,2) NOT NULL,
    coverage_start    DATE NOT NULL,
    coverage_end      DATE NOT NULL,                -- Always 7 days later
    status            ENUM('ACTIVE','PAUSED','EXPIRED','CANCELLED') DEFAULT 'ACTIVE',
    auto_renew        BOOLEAN DEFAULT TRUE,
    FOREIGN KEY (worker_id) REFERENCES users(id)
);

-- Auto-generated disruption events
CREATE TABLE disruption_events (
    id             BIGINT AUTO_INCREMENT PRIMARY KEY,
    event_type     ENUM('HEAVY_RAIN','FLOOD','EXTREME_HEAT','SEVERE_AQI','CIVIC') NOT NULL,
    zone_id        BIGINT NOT NULL,
    triggered_at   TIMESTAMP NOT NULL,
    ended_at       TIMESTAMP,
    severity_value DECIMAL(10,2),                  -- 42.3mm/hr, 46°C, AQI 450, etc.
    data_source    VARCHAR(100),
    is_verified    BOOLEAN DEFAULT TRUE,
    FOREIGN KEY (zone_id) REFERENCES zones(id)
);

-- Claims (auto-created, never filed manually)
CREATE TABLE claims (
    id                    BIGINT AUTO_INCREMENT PRIMARY KEY,
    worker_id             BIGINT NOT NULL,
    policy_id             BIGINT NOT NULL,
    disruption_event_id   BIGINT NOT NULL,
    payout_amount         DECIMAL(10,2) NOT NULL,
    fraud_score           DECIMAL(5,2) DEFAULT 0,
    status                ENUM('AUTO_APPROVED','PENDING_REVIEW','APPROVED','REJECTED') NOT NULL,
    rejection_reason      VARCHAR(255),
    created_at            TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (worker_id) REFERENCES users(id),
    FOREIGN KEY (policy_id) REFERENCES policies(id),
    FOREIGN KEY (disruption_event_id) REFERENCES disruption_events(id)
);

-- Payouts
CREATE TABLE payouts (
    id              BIGINT AUTO_INCREMENT PRIMARY KEY,
    claim_id        BIGINT NOT NULL,
    worker_id       BIGINT NOT NULL,
    amount          DECIMAL(10,2) NOT NULL,
    upi_id          VARCHAR(100) NOT NULL,
    razorpay_txn_id VARCHAR(100),
    status          ENUM('INITIATED','PROCESSING','SUCCESS','FAILED') NOT NULL,
    initiated_at    TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    completed_at    TIMESTAMP,
    FOREIGN KEY (claim_id) REFERENCES claims(id)
);

-- AI premium audit log (every calculation stored)
CREATE TABLE premium_calculations (
    id              BIGINT AUTO_INCREMENT PRIMARY KEY,
    worker_id       BIGINT NOT NULL,
    week_start_date DATE NOT NULL,
    base_premium    DECIMAL(10,2),
    adjustment      DECIMAL(10,2),
    final_premium   DECIMAL(10,2),
    factors_json    JSON,              -- Stores all 11 input features
    calculated_at   TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Fraud check logs
CREATE TABLE fraud_logs (
    id                    BIGINT AUTO_INCREMENT PRIMARY KEY,
    claim_id              BIGINT NOT NULL,
    worker_id             BIGINT NOT NULL,
    fraud_score           DECIMAL(5,2),
    flags_triggered       JSON,        -- Which hard rules fired
    gps_lat               DECIMAL(10,8),
    gps_lng               DECIMAL(11,8),
    distance_from_zone_km DECIMAL(10,2),
    reviewed              BOOLEAN DEFAULT FALSE,
    created_at            TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

---

## 📁 Project Structure

```
gigshield/
│
├── 📁 frontend/                         ← React + Tailwind
│   └── src/
│       ├── components/
│       │   ├── auth/                    ← OTP Login, Register
│       │   ├── onboarding/              ← 5-step worker setup
│       │   ├── policy/                  ← Plan selection, premium card, renewal
│       │   ├── claims/                  ← Claim list, status, payout tracker
│       │   ├── dashboard/               ← Worker home, Admin panel, charts
│       │   └── common/                  ← Navbar, Spinner, Protected routes
│       ├── services/                    ← Axios API calls (auth, policy, claims)
│       ├── store/                       ← Zustand (auth, user state)
│       └── utils/                       ← Currency formatter, date helpers
│
├── 📁 backend/                          ← Spring Boot
│   └── src/main/java/com/gigshield/
│       ├── controller/                  ← REST endpoints
│       ├── service/                     ← Business logic
│       ├── repository/                  ← JPA repos (DB queries)
│       ├── model/                       ← JPA entity classes
│       ├── dto/                         ← Request/Response objects
│       ├── scheduler/
│       │   ├── DisruptionMonitorJob.java  ← Runs every 15 min
│       │   └── WeeklyRenewalJob.java      ← Runs Sunday midnight
│       ├── security/                    ← JWT filter + Spring Security config
│       ├── integration/                 ← API clients (weather, AQI, Razorpay)
│       └── exception/                   ← Global error handling
│
├── 📁 database/
│   └── schema.sql                       ← Full MySQL schema
│
├── 📁 ml/                               ← AI/ML scripts (Phase 2–3)
│   ├── premium_model.py                 ← XGBoost training + export
│   ├── fraud_model.py                   ← Isolation Forest
│   └── requirements.txt
│
└── README.md
```
ML Folder Structure Explained:
```
📁 ml/
├── 📁 notebooks/
│   ├── 01_data_exploration.ipynb       ← EDA: weather patterns, disruption frequency,
│   │                                      zone risk heatmaps, income loss correlations
│   ├── 02_severity_classifier.ipynb    ← Train Random Forest to classify disruption
│   │                                      severity: MILD / MODERATE / SEVERE
│   ├── 03_loss_estimator.ipynb         ← Predict actual income loss (₹) given a
│   │                                      disruption type, zone, and duration
│   ├── 04_premium_model.ipynb          ← Train XGBoost to calculate personalized
│   │                                      weekly premium adjustments per worker
│   └── 05_fraud_detection.ipynb        ← Train Isolation Forest anomaly detector,
│                                          tune contamination factor, plot score dist.
│
├── 📁 data/
│   ├── raw/                            ← Historical weather data (IMD, OpenWeatherMap)
│   │   ├── bangalore_weather_2023.csv      rainfall, temperature by zone, daily
│   │   ├── delhi_aqi_2023.csv              AQI readings by zone, hourly
│   │   ├── mumbai_flood_events.csv         flood advisory records
│   │   └── citywise_disruption_log.csv     aggregated disruption events
│   │
│   ├── processed/                      ← Cleaned, feature-engineered datasets
│   │   ├── features_premium.csv            ready-to-train premium model features
│   │   ├── features_fraud.csv              fraud detection feature matrix
│   │   └── features_severity.csv           severity classifier training data
│   │
│   └── synthetic/                      ← Generated training records
│       ├── synthetic_claims.csv            10,000 fake claim records with labels
│       ├── synthetic_fraud_cases.csv       labelled fraud + legit cases for training
│       └── GENERATION_NOTES.md            explains how synthetic data was created
│
├── 📁 models/                          ← Saved trained model files
│   ├── severity_clf.pkl                ← Random Forest severity classifier
│   ├── loss_estimator.pkl              ← Regression model for income loss (₹)
│   ├── premium_model.pkl               ← XGBoost premium adjustment calculator
│   └── fraud_detector.pkl              ← Isolation Forest fraud scorer
│
├── api.py                              ← Flask app — exposes all 4 models as REST endpoints
├── train.py                            ← Full training pipeline — run once to regenerate all .pkl
├── requirements.txt                    ← All Python dependencies
└── README.md                           ← How to run notebooks, train, and start the API
```
---

## 🔌 Key API Endpoints

### Worker APIs

| Method | Endpoint | Description |
|--------|----------|-------------|
| `POST` | `/api/auth/send-otp` | Send OTP to mobile |
| `POST` | `/api/auth/verify-otp` | Verify OTP → receive JWT |
| `POST` | `/api/workers/register` | Complete worker profile |
| `GET` | `/api/workers/me/dashboard` | Home screen data |
| `GET` | `/api/policies/plans` | Tier options + personalized prices |
| `POST` | `/api/policies/create` | Purchase a plan |
| `GET` | `/api/policies/active` | Current policy status |
| `GET` | `/api/premium/quote` | This week's AI-adjusted premium |
| `GET` | `/api/premium/factors` | Why your premium changed |
| `GET` | `/api/claims` | Claim history + payout status |
| `GET` | `/api/disruptions/active` | Live events in your zone |

### Admin APIs

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/api/admin/dashboard` | KPIs: policies, claims, loss ratio, payouts |
| `GET` | `/api/admin/claims/pending` | Manual review queue |
| `PUT` | `/api/admin/claims/{id}/approve` | Approve a flagged claim |
| `PUT` | `/api/admin/claims/{id}/reject` | Reject with reason |
| `GET` | `/api/admin/disruptions/live` | Real-time disruption monitor |
| `GET` | `/api/admin/fraud/logs` | Fraud detection audit trail |
| `GET` | `/api/admin/analytics/forecast` | 7-day payout risk forecast |

---

## 📅 Development Plan

### Phase 1 — Ideation & Foundation (March 4–20) ✅ Current Phase

| Task | Status | Deadline |
|------|--------|----------|
| Persona research and scenario definition | ✅ Done | Mar 7 |
| Weekly premium model design | ✅ Done | Mar 10 |
| Parametric trigger specification (5 triggers) | ✅ Done | Mar 10 |
| System architecture design | ✅ Done | Mar 12 |
| Full database schema design | ✅ Done | Mar 14 |
| GitHub repo + detailed README | ✅ Done | Mar 18 |
| React + Vite project scaffolding | 🔄 In Progress | Mar 19 |
| Spring Boot project + Flyway migration | 🔄 In Progress | Mar 19 |
| 2-minute strategy video recording | 🔲 Pending | **Mar 20** |

---

### Phase 2 — Automation & Protection (March 21 – April 4)

**Theme: "Make the Platform Work"**

| Feature | Priority | Notes |
|---------|---------|-------|
| OTP-based registration (SMS mock) | P0 | Core onboarding |
| JWT authentication — Spring Security | P0 | Secure all endpoints |
| Worker onboarding UI — 5 steps | P0 | Mobile-first Tailwind |
| Zone selection — city + area picker | P1 | Dropdown or map |
| Policy creation + tier selection UI | P0 | Show personalized prices |
| AI Premium Calculator — rule-based v1 | P0 | Weighted scoring |
| Spring Scheduler — disruption monitor | P0 | 15-min polling |
| Trigger 1 + 2: Rain + Heat (OpenWeatherMap) | P0 | Real API |
| Triggers 3, 4, 5: AQI, Flood, Civic (mock) | P1 | Mocked JSON |
| Auto-claim creation on trigger | P0 | Core parametric logic |
| Basic fraud validation (hard rules) | P0 | GPS, duplicate check |
| Razorpay test mode payout | P1 | Sandbox integration |
| Worker dashboard — coverage + claims | P0 | Home screen |
| 2-minute demo video | P0 | **Due April 4** |

---

### Phase 3 — Scale & Optimise (April 5–17)

**Theme: "Make It Production-Ready"**

| Feature | Priority | Notes |
|---------|---------|-------|
| ML Fraud Detection — Isolation Forest | P0 | Python model → REST API |
| GPS spoofing detection | P0 | Trajectory anomaly logic |
| XGBoost premium model integration | P1 | Replace rule-based v1 |
| Razorpay webhooks — confirmed payouts | P0 | Full payout lifecycle |
| Worker dashboard — protected earnings view | P0 | "You've saved ₹2,400 this month" |
| Admin dashboard — loss ratio, analytics | P0 | Charts + tables |
| Admin fraud review queue | P0 | Approve/reject with reason |
| Predictive risk forecast (admin) | P1 | 7-day zone risk |
| Weekly renewal automation | P0 | Sunday midnight scheduler |
| Language toggle (Hindi) | P2 | i18n support |
| Final 5-minute demo video | P0 | **Due April 17** |
| Final pitch deck (PDF) | P0 | **Due April 17** |

---

## 💹 Business Viability

### Unit Economics — Per Worker (Standard Plan)

```
Weekly premium collected:    ₹59
Expected claim payout:       ₹22   (37% loss ratio — industry standard for parametric)
Platform + infra cost:       ₹8
───────────────────────────────
Net margin per worker/week:  ₹29   (49%)
```

### Revenue Projections

| Active Workers | Weekly Revenue | Annual Revenue |
|---------------|----------------|----------------|
| 10,000 | ₹5.9 Lakh | ₹3.07 Crore |
| 1,00,000 | ₹59 Lakh | ₹30.7 Crore |
| 5,00,000 | ₹2.95 Crore | ₹153 Crore |

### Why This Business Makes Sense

**1. Parametric = No investigation costs**
Traditional insurance companies spend 30–40% of premiums on claims investigation. Parametric eliminates this entirely — payouts are triggered by data, not human review.

**2. AI pricing = No adverse selection**
Without personalization, high-risk workers buy and low-risk workers don't. AI pricing ensures every zone pays a fair rate — protecting the loss ratio.

**3. Weekly model = Low churn**
Workers aren't locked in. A bad month doesn't mean losing the customer forever — they can pause and return. This builds long-term trust.

**4. Platform partnerships = Distribution at scale**
Swiggy and Zomato have a direct incentive to offer GigShield as a partner benefit. It makes their workers more financially resilient and more likely to stay on the platform. One partnership could unlock access to millions of delivery partners overnight.

**5. Market gap = No direct competitor**
No existing product in India covers parametric income insurance specifically for food delivery partners. GigShield is a first-mover.

---

## ⚙️ Setup & Installation

### What You Need

```
Node.js    v18+      (for React frontend)
Java       17 LTS    (for Spring Boot backend)
Maven      3.8+      (for Java build)
MySQL      8.0+      (for database)
Git        Latest
```

### Step 1 — Clone the Repository

```bash
git clone https://github.com/SagnikPratihar/gigshield.git
cd gigshield
```

### Step 2 — Set Up the Database

```bash
mysql -u root -p

CREATE DATABASE gigshield CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
CREATE USER 'gigshield_user'@'localhost' IDENTIFIED BY 'gigshield_pass';
GRANT ALL PRIVILEGES ON gigshield.* TO 'gigshield_user'@'localhost';
FLUSH PRIVILEGES;
EXIT;

# Flyway will auto-run the migration on first Spring Boot startup
```

### Step 3 — Configure & Run the Backend

```bash
cd backend

# Edit: src/main/resources/application-dev.properties

spring.datasource.url=jdbc:mysql://localhost:3306/gigshield
spring.datasource.username=gigshield_user
spring.datasource.password=gigshield_pass
jwt.secret=YOUR_256_BIT_SECRET_KEY_HERE
openweather.api.key=YOUR_OPENWEATHERMAP_FREE_KEY
razorpay.key.id=YOUR_RAZORPAY_TEST_KEY_ID
razorpay.key.secret=YOUR_RAZORPAY_TEST_SECRET

# Build and start
mvn clean install -DskipTests
mvn spring-boot:run -Dspring-boot.run.profiles=dev

# ✅ Backend running at: http://localhost:8080
```

### Step 4 — Configure & Run the Frontend

```bash
cd frontend

npm install

# Edit: .env
VITE_API_BASE_URL=http://localhost:8080/api
VITE_APP_NAME=GigShield
VITE_WEATHER_API_KEY=YOUR_OPENWEATHERMAP_FREE_KEY

npm run dev

# ✅ Frontend running at: http://localhost:5173
```

### Step 5 — Verify Everything Works

```bash
# Check backend health
curl http://localhost:8080/api/health
# Expected: { "status": "UP", "database": "Connected" }

# Open the worker app
open http://localhost:5173

# Open the admin panel
open http://localhost:5173/admin
```

### Getting Free API Keys

| API | Where to Get | Notes |
|-----|-------------|-------|
| OpenWeatherMap | [openweathermap.org/api](https://openweathermap.org/api) | Free tier: 1M calls/month |
| Razorpay Test | [dashboard.razorpay.com](https://dashboard.razorpay.com) | Test keys — no real money |

---

## ⚠️ Risks & How We Handle Them

| Risk | How Likely | How We Mitigate It |
|------|-----------|-------------------|
| Weather API rate limits hit | Medium | Cache response per zone per 15 min; batch all zone polls in one call |
| GPS spoofing fraud at scale | High | Multi-layer: hard rules + ML score + device fingerprint |
| Workers don't understand parametric | High | Plain language: "You get paid automatically when it rains hard" — no jargon |
| UPI payout failure | Low | Retry mechanism (3 attempts), then SMS fallback + manual queue |
| Adverse selection (only risky zones buy) | Medium | AI pricing adjusts for zone risk — neutralizes adverse selection |
| Platform API not available | High | All platform integrations are mocked — zero dependency |

---

## 👥 Team

| Name | 
|------|
| Soumyajit Rout  | Team Lead |
| Sagnik Pratihar | 
| Aneek Mukherjee |
| Bijay Mahato    | 

---

## 📎 Submission Links

| Deliverable | Link | Status |
|------------|------|--------|
| 🎥 Phase 1 — 2-min Strategy Video | TBD | 🔲 Due March 20 |
| 🎥 Phase 2 — 2-min Demo Video | TBD | 🔲 Due April 4 |
| 🎥 Phase 3 — 5-min Final Demo | TBD | 🔲 Due April 17 |
| 📊 Final Pitch Deck (PDF) | TBD | 🔲 Due April 17 |
| 🌐 Live Demo | TBD | 🔲 Phase 3 |
| 💻 GitHub Repository | This Repo | ✅ Live |

---

<div align="center">

---

### 🛡️ GigShield — Because Every Shift Deserves a Safety Net

*Built for Guidewire DEVTrails 2026 · Seed. Scale. Soar.*

![React](https://img.shields.io/badge/React_18-61DAFB?logo=react&logoColor=black&style=flat-square)
![Spring Boot](https://img.shields.io/badge/Spring_Boot_3.2-6DB33F?logo=springboot&logoColor=white&style=flat-square)
![MySQL](https://img.shields.io/badge/MySQL_8.0-4479A1?logo=mysql&logoColor=white&style=flat-square)
![Tailwind CSS](https://img.shields.io/badge/Tailwind_CSS_3-06B6D4?logo=tailwindcss&logoColor=white&style=flat-square)
![Java](https://img.shields.io/badge/Java_17-ED8B00?logo=openjdk&logoColor=white&style=flat-square)

</div>
