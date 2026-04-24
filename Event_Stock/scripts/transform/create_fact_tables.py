import pandas as pd

stock = pd.read_csv('data/silver/stock_clean.csv')
news = pd.read_csv('data/silver/news_clean.csv')

# Example fact table
fact_stock = stock[['symbol','trade_date','open_price','close_price','volume']]

fact_stock.to_csv('data/gold/fact_stock_market.csv', index=False)

print("Gold tables created")