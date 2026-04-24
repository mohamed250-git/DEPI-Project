import requests
import pandas as pd
from pathlib import Path
from datetime import datetime
import json
import os

# =====================================================
# CONFIG
# =====================================================
NEWS_API_KEY="71cfd17a96b9419bb6add03d8876b889"  # set env variable
BASE_URL = "https://newsapi.org/v2/everything"

# =====================================================
# FORWARD-LOOKING MARKET MOVING EVENTS
# (focus on upcoming / developing risks & catalysts)
# =====================================================
topics = {
    "Monetary_Policy": [
        "Federal Reserve next meeting",
        "Fed rate decision upcoming",
        "ECB next interest rate decision",
        "Bank of England next meeting",
        "central bank guidance",
        "interest rate cuts expected",
        "inflation report upcoming",
        "CPI release next week",
        "jobs report upcoming"
    ],

    "Politics_Elections": [
        "upcoming election markets",
        "US election polls",
        "presidential debate upcoming",
        "parliament vote next week",
        "government shutdown risk",
        "debt ceiling negotiations",
        "new sanctions expected",
        "trade agreement talks"
    ],

    "Geopolitics": [
        "Middle East tensions rising",
        "China Taiwan military drills",
        "Russia Ukraine escalation risk",
        "shipping route disruption",
        "new tariffs expected",
        "border conflict tensions"
    ],

    "Economic_Risk": [
        "recession risk 2026",
        "banking sector stress warning",
        "commercial real estate risk",
        "consumer spending slowdown",
        "GDP slowdown forecast",
        "credit default concerns",
        "currency crisis warning"
    ],

    "Corporate_Catalysts": [
        "earnings next week",
        "major IPO upcoming",
        "merger talks reported",
        "stock buyback announced",
        "guidance cut expected",
        "layoffs announced tech sector"
    ],

    "Technology_AI": [
        "AI regulation upcoming",
        "chip export restrictions expected",
        "semiconductor shortage warning",
        "cybersecurity threat alert",
        "big tech antitrust case"
    ],

    "Energy_Commodities": [
        "OPEC meeting upcoming",
        "oil supply disruption risk",
        "natural gas shortage warning",
        "gold rally safe haven",
        "copper demand forecast"
    ],

    "Health_Global": [
        "WHO emergency warning",
        "new virus outbreak monitoring",
        "pandemic preparedness alert",
        "drug pricing regulation upcoming"
    ],

    "Climate_Disaster": [
        "hurricane season forecast",
        "wildfire risk warning",
        "drought impact crops",
        "flooding supply chain risk",
        "earthquake disruption risk"
    ],

    "Market_Sentiment": [
        "stock market volatility expected",
        "investor risk off sentiment",
        "VIX spike warning",
        "market correction fears",
        "bull market outlook"
    ]
}

# =====================================================
# DATE
# =====================================================
run_date = datetime.now().strftime("%Y-%m-%d")

# =====================================================
# FETCH NEWS
# =====================================================
def fetch_news(query):
    params = {
        "q": query,
        "language": "en",
        "sortBy": "publishedAt",
        "pageSize": 20,
        "searchIn": "title,description",
        "apiKey": NEWS_API_KEY
    }

    r = requests.get(BASE_URL, params=params, timeout=30)
    r.raise_for_status()
    return r.json()

# =====================================================
# RUN
# =====================================================
for category, keywords in topics.items():

    for keyword in keywords:
        try:
            print(f"Downloading: {keyword}")

            safe_keyword = keyword.replace(" ", "_").replace("/", "_")

            output_dir = Path(
                f"data/bronze/news/category={category}/topic={safe_keyword}/{run_date}"
            )

            output_dir.mkdir(parents=True, exist_ok=True)

            data = fetch_news(keyword)

            # Save raw API response
            with open(output_dir / "news.json", "w", encoding="utf-8") as f:
                json.dump(data, f, indent=2, ensure_ascii=False)

            # Flatten articles
            articles = data.get("articles", [])

            if articles:
                rows = []

                for a in articles:
                    rows.append({
                        "category": category,
                        "keyword": keyword,
                        "source": a["source"]["name"],
                        "author": a["author"],
                        "title": a["title"],
                        "description": a["description"],
                        "url": a["url"],
                        "publishedAt": a["publishedAt"],
                        "content": a["content"]
                    })

                df = pd.DataFrame(rows)
                df.to_parquet(output_dir / "articles.parquet", index=False)

            print(f"Saved: {keyword}")

        except Exception as e:
            print(f"Failed {keyword}: {e}")