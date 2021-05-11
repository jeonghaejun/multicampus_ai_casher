import json

def lambda_handler(event, context):
    # TODO implement
    
    storageInfo = event['Records'][0].get('s3')
    
    print(storageInfo['object']['key'])
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
