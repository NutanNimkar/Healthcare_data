import boto3
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# AWS S3 credentials
AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')
AWS_REGION = os.getenv('AWS_REGION')
S3_BUCKET_NAME = os.getenv('S3_BUCKET_NAME')

s3_client = boto3.client(
    's3',
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
    region_name=AWS_REGION
)

file_path = 'data/cleaned_healthcare_data.csv'  # Path to your cleaned data file
s3_key = 'healthcare_data/cleaned_healthcare_data.csv'  # S3 file path (key)

try:
    s3_client.upload_file(file_path, S3_BUCKET_NAME, s3_key)
    print(f"File successfully uploaded to S3: s3://{S3_BUCKET_NAME}/{s3_key}")
except Exception as e:
    print(f"Error uploading file to S3: {e}")