import json
import boto3
from botocore.config import Config
import pymysql
import os
import time


my_config = Config(
    region_name='eu-west-2',
    signature_version='v4',
    retries={
        'max_attempts': 10,
        'mode': 'standard'
    }
    )




def lambda_handler(event, context):
    conn = pymysql.connect(
    host=os.environ['DB_HOST'], port=3306, user='admin', passwd=os.environ['DB_PW'], db='multicampus', charset='utf8')
    cursor = conn.cursor()
    
    client = boto3.client('sns',config=my_config)
    print(event)
    
    phone_number = event["phonenum"]
    phone_arr = phone_number.split('-')
    phone_number = "+8210" + phonenum[1] + phone_arr[2] 
    msg = "계산 내역입니다.\n"
    print(phone_number)
    
    for item in event["item"]:
        sql = "SELECT Product_name FROM Item_info WHERE Item_id={}"
        sql = sql.format(item["id"])

        cursor.execute(sql)
        result = cursor.fetchall()
        
        msg += str(result[0][0]) + ", " + str(item["Qty"]) + "개 구매하셨습니다.\n"
        
    try:
        response = client.publish(
            PhoneNumber = phone_number,
            Message=f'[빨리캐셔 모바일 영수증]\n{msg}',
        )
        print(f'send to {phone_number}')
        print(response)
    except:
        print(f'can not send to {phone_number}')
    
    finally:
        conn.close()

    return {
        'statusCode': 200,
        'body': json.dumps(result)
        
    }