import boto3
# S3 클라이언트 생성 
s3 = boto3.client('s3') # create_bucket()를 통해 버킷 생성. 
s3.create_bucket(Bucket='minjutest-bucket' , CreateBucketConfiguration={'LocationConstraint': 'ap-northeast-2'})

print('s3')