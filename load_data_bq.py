from google.cloud import bigquery
import os

# Set environment variables for project and bucket
DATASET_NAME = 'sandbox'
PROJECT_ID = os.getenv('GCP_PROJECT')
BUCKET_NAME = os.getenv('GCS_BUCKET')
TABLE_NAME = 'my_table'

def load_data_to_bigquery(df):
    """Load data from a Pandas DataFrame to BigQuery."""
    client = bigquery.Client()
    table_id = f"{PROJECT_ID}.{DATASET_NAME}.{TABLE_NAME}"
    
    # Load data to BigQuery
    job_config = bigquery.LoadJobConfig(
        write_disposition=bigquery.WriteDisposition.WRITE_APPEND,
        autodetect=True
    )
    
    job = client.load_table_from_dataframe(df, table_id, job_config=job_config)
    job.result()  # Wait for the job to complete