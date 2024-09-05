# G-Cloud-Function-DataLoad-Pipeline

This repository contains code for a Google Cloud Function that automatically loads data from Google Cloud Storage (GCS) into BigQuery. The function is triggered by changes in a GCS bucket, reads the file as a Pandas DataFrame, and loads the data into a BigQuery table.

## Folder Structure

- **load_data_bq.py**: Contains the function to load data from a Pandas DataFrame into BigQuery.
- **read_files_gcs.py**: Contains the function to read a file from Google Cloud Storage and convert it into a Pandas DataFrame.
- **main.py**: Entry point for the Google Cloud Function, integrating the functions from `load_data_bq.py` and `read_files_gcs.py`.
- **requirements.txt**: Lists the Python dependencies required for the Cloud Function.

## Setup

### Prerequisites

- Google Cloud Project with billing enabled
- Google Cloud Storage bucket
- BigQuery dataset and table created

### Environment Variables

Set the following environment variables in your Google Cloud Function:
- `GCP_PROJECT`: Your Google Cloud project ID.
- `GCS_BUCKET`: The name of your Google Cloud Storage bucket.

### Dependencies

The `requirements.txt` file includes the necessary dependencies:
- `functions-framework`: For running the function locally.
- `google-cloud-storage`: For interacting with Google Cloud Storage.
- `google-cloud-bigquery`: For interacting with BigQuery.
- `pyarrow`: Required for working with BigQuery.
- `pandas`: For data manipulation.

To install the dependencies, run:

```sh
pip install -r requirements.txt
```
### Deployment
Zip the project folder, including main.py, load_data_bq.py, read_files_gcs.py, and requirements.txt.

**Deploy the Cloud Function using the following command:**
```
gcloud functions deploy gcs_to_bigquery \
    --runtime python311 \
    --trigger-resource YOUR_BUCKET_NAME \
    --trigger-event google.storage.object.finalize \
    --entry-point gcs_to_bigquery \
    --memory 256MB \
    --region YOUR_REGION
```
Replace `YOUR_BUCKET_NAME` with the name of your GCS bucket and `YOUR_REGION` with the appropriate region for your function.

### Functionality
**Trigger**: The function is triggered by file uploads or changes in the specified GCS bucket.
**Processing**: Reads the file from GCS, converts it to a Pandas DataFrame, and loads it into the specified BigQuery table.

Notes
Ensure that the Cloud Function has the necessary permissions to read from GCS and write to BigQuery.
Adjust the memory settings as needed based on the size of your data.
