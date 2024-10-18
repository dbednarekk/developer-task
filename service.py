import re

FOLDER_PREFIX = "TIE-rp"


# List all objects in a bucket with prefix "TIE-rp"
def list_all_bucket_objects(bucket):
    try:
        for my_bucket_object in bucket.objects.filter(Prefix=FOLDER_PREFIX):
            print(my_bucket_object.key)
    except Exception as e:
        print(f"Error during listing files in folder {FOLDER_PREFIX} : {e}")


# Upload file to a specific folder in the bucket
def upload_file_to_bucket(bucket, file_path, destination_path):
    try:
        bucket.upload_file(file_path, f"TIE-rp/{destination_path}")
        print("File uploaded successfully")
    except FileNotFoundError as e:
        print(f"File not found, error below: \n {e}")
    except Exception as e:
        print(f"Error during uploading file to location: {destination_path}: {e}")


# List files in a bucket with a specific filter
def list_bucket_files(bucket, filter_regex):
    for my_bucket_object in bucket.objects.filter(Prefix=FOLDER_PREFIX):
        if re.search(filter_regex, my_bucket_object.key):
            print(my_bucket_object.key)


# Delete file from a bucket with a specific path
def delete_file_from_bucket(bucket, regex):
    try:
        for my_bucket_object in bucket.objects.filter(Prefix=FOLDER_PREFIX):
            if re.search(regex, my_bucket_object.key):
                my_bucket_object.delete()
                print("File deleted successfully")
    except Exception as e:
        print(f"Error during removing files matching regex: {regex}: {e}")
