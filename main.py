import boto3
import service
from dotenv import load_dotenv
import os

#Load the environment variables for AWS credentials
load_dotenv()

# Create a session using your AWS credentials and specify s3 instance
session = boto3.Session(aws_access_key_id=os.getenv("AWS_ACCESS_KEY"), aws_secret_access_key=os.getenv("AWS_SECRET_KEY"))
s3 = session.resource('s3')
dev_bucket = s3.Bucket('developer-task2')


service.upload_file_to_bucket(dev_bucket, 'upload_test.txt', 'TIE-rp/upload/upload_test.txt')


service.list_all_bucket_objects(dev_bucket)



service.delete_file_from_bucket(dev_bucket, 'TIE-rp/upload/upload_test.txt')

FILTER = "tes"

service.list_bucket_files(dev_bucket, FILTER)