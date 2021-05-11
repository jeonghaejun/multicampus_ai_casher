import boto3

s3 = boto3.client('s3')

filename = 'puppy_1.mp4'

bucket_name = 'test-bucket4boto3'
s3.upload_file(filename,bucket_name,filename)

# https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.Client.put_object_acl
response = s3.put_object_acl(ACL='public-read', Bucket=bucket,Key=key)
print(response)
# TODO: 버킷 권한 설정

print('success')