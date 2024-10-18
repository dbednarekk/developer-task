import os

import boto3
from dotenv import load_dotenv

import argument_parser
import service

arguments = argument_parser.python_Arg()

# Load the environment variables for AWS credentials
load_dotenv()
# Create a session using your AWS credentials and specify s3 instance
session = boto3.Session(
    aws_access_key_id=os.getenv("AWS_ACCESS_KEY"),
    aws_secret_access_key=os.getenv("AWS_SECRET_KEY"),
)
s3 = session.resource("s3")
dev_bucket = s3.Bucket("developer-task2")

#Probably a for loop would be better here if you want to run multiple commands, but it wasn't specified
if arguments.list:
    service.list_all_bucket_objects(dev_bucket)

if arguments.upload:
    service.upload_file_to_bucket(dev_bucket, arguments.upload[0], arguments.upload[1])

if arguments.filter:
    service.list_bucket_files(dev_bucket, arguments.filter)

if arguments.delete:
    service.delete_file_from_bucket(dev_bucket, arguments.delete)
