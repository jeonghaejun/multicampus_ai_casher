from json import dumps, loads
from botocore.vendored import requests
import pymysql
import json


#from flask import Response
conn = pymysql.connect()

def lambda_handler(event, context):
   
    cursor = conn.cursor()

    item = {}
    params_array = event['params']
    path_array = params_array['path']
    item_no = (path_array['item-no'])
    
    print(event)

    sql = "SELECT * FROM Item_info WHERE Item_id={}"
    sql = sql.format(item_no)

    cursor.execute(sql)
    conn.commit()
    result = cursor.fetchall()
    result_list = []
    result_list = list(result[0])

    item['name'] = result_list[1]
    item['price'] = result_list[2]
    

    return {
        'statusCode': 200,
        'body': json.dumps(event)
    }
