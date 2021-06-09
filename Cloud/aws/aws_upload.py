import boto3
s3 = boto3.client('s3')
Response = s3.list_buckets()

buckets = [bucket['Name'] for bucket in Response['Buckets']]
print("Bucket List: %s" % buckets)

