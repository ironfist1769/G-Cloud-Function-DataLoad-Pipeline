from google.cloud import storage
import pandas as pd
from io import StringIO

def read_file_from_gcs(bucket_name, file_name):
    """Read file from Google Cloud Storage and return it as a Pandas DataFrame."""
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(file_name)
    
    # Download the file contents
    file_contents = blob.download_as_text()
    
    # Assuming the file is CSV; adjust if the format is different
    data = StringIO(file_contents)
    df = pd.read_csv(data)
    
    return df