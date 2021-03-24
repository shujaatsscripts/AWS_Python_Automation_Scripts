import logging
import boto3
from botocore.exceptions import ClientError


bucket_name = "Test_Bucket" #Aws bucket name
file_name = "TEST.txt" #Filename with extension
file_path = "C:/Users/Username/Desktop/" + file_name  #Path to the file

print(file_path)
obj_name = ""  #Aws object name optional

def upload_file(file_path, file_name, bucket, object_name=None):
    # """Upload a file to an S3 bucket

    # :param file_name: File to upload
    # :param bucket: Bucket to upload to
    # :param object_name: S3 object name. If not specified then file_name is used
    # :return: True if file was uploaded, else False
    # """

    # If S3 object_name was not specified, use file_name
    if object_name is None:
        object_name = file_name

    # Upload the file
    s3_client = boto3.client('s3')
    try:
        response = s3_client.upload_file(file_path, bucket, object_name)
        print("File Uploaded")
    except ClientError as e:
        logging.error(e)
        return False
    return True



upload_file(file_path, file_name, bucket_name)
