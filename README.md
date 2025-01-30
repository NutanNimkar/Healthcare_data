Healthcare Data Pipeline
This project is a Python-based pipeline that reads cleaned healthcare data from a CSV file and uploads it to an AWS S3 bucket. It uses pandas for data manipulation, boto3 for interacting with AWS S3, and python-dotenv for managing environment variables.
Project Overview
The pipeline performs the following tasks:

Reads cleaned healthcare data from a CSV file (data/cleaned_healthcare_data.csv).

Connects to an AWS S3 bucket using credentials stored in a .env file.

Uploads the CSV file to the specified S3 bucket.
