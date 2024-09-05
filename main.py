import functions_framework

from load_data_bq import load_data_to_bigquery
from read_file_gcs import read_file_from_gcs


@functions_framework.cloud_event
def gcs_to_bigquery(cloud_event):
    """Triggered by a change in a storage bucket."""
    data = cloud_event.data

    bucket = data["bucket"]
    name = data["name"]

    print(f"Bucket: {bucket}")
    print(f"File: {name}")

    # Read the file from GCS and load into BigQuery
    df = read_file_from_gcs(bucket, name)
    load_data_to_bigquery(df)