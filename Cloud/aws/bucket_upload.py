import boto3
import time
s3 = boto3.client('s3',aws_access_key_id='',
                  aws_secret_access_key='') # github 같은 public repo에 올릴때 같이 올리지 않도록 주의!



filename = 'hellyeah.jpg'  
# 로컬에서 올릴 파일 및 경로 이름

bucket_name = 'yangjae-team07-bucket'

key = "test.jpg" # S3에 올릴 때 이름

s3.upload_file(filename, bucket_name, key)

# https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.Client.put_object_acl
response = s3.put_object_acl(ACL='public-read', Bucket=bucket_name, Key=key)

print(response)
