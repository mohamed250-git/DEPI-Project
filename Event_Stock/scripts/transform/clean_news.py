import pandas as pd

df = pd.read_csv('data/bronze/news_raw.csv')

df.drop_duplicates(inplace=True)

df.to_csv('data/silver/news_clean.csv', index=False)

print("News cleaned")