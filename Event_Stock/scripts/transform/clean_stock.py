import pandas as pd

df = pd.read_csv('data/bronze/stock_prices_raw.csv')

df.columns = df.columns.str.lower()

df.rename(columns={
    'date':'trade_date',
    'open':'open_price',
    'close':'close_price'
}, inplace=True)

df.drop_duplicates(inplace=True)

df.to_csv('data/silver/stock_clean.csv', index=False)

print("Stock cleaned")