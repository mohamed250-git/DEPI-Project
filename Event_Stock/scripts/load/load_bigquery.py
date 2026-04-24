from google.cloud import bigquery

client = bigquery.Client()

table_id = "your-project-id.finance.fact_stock_market"

job_config = bigquery.LoadJobConfig(
    source_format=bigquery.SourceFormat.CSV,
    skip_leading_rows=1,
    autodetect=True
)

with open("data/gold/fact_stock_market.csv", "rb") as file:
    job = client.load_table_from_file(file, table_id, job_config=job_config)

job.result()

print("Loaded to BigQuery")