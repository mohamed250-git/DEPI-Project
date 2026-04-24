import yfinance as yf
import pandas as pd
from pathlib import Path
from datetime import datetime
import json

# -----------------------------------
# Companies grouped by industry
# -----------------------------------
tickers = {
    "Technology": ["AAPL", "MSFT", "NVDA", "GOOGL"],
    "Finance": ["JPM", "BAC", "GS"],
    "Energy": ["XOM", "CVX"],
    "Healthcare": ["JNJ", "PFE"],
    "Consumer": ["AMZN", "WMT", "KO"],
    "Transport": ["TSLA", "UPS"]
}

# Run date
run_date = datetime.now().strftime("%Y-%m-%d")

# -----------------------------------
# Loop through sectors + companies
# -----------------------------------
for sector, symbols in tickers.items():

    for ticker_symbol in symbols:
        try:
            print(f"Downloading {ticker_symbol}...")

            # Bronze path
            output_dir = Path(
                f"data/bronze/yahoo_finance/sector={sector}/symbol={ticker_symbol}/{run_date}"
            )

            output_dir.mkdir(parents=True, exist_ok=True)

            # Yahoo extract
            ticker = yf.Ticker(ticker_symbol)

            hist = ticker.history(period="1mo", interval="1d")
            info = ticker.info

            # Save prices
            hist.reset_index().to_parquet(
                output_dir / "prices.parquet",
                index=False
            )

            # Save metadata
            with open(output_dir / "info.json", "w") as f:
                json.dump(info, f, indent=2, default=str)

            print(f"Saved {ticker_symbol}")

        except Exception as e:
            print(f"Failed {ticker_symbol}: {e}")