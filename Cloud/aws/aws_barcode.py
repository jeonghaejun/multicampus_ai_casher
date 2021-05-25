from json import dumps, loads
from botocore.vendored import requests
import pymysql
import json

#from flask import Response
conn = pymysql.connect(
    host=os.environ['DB_HOST'], port=3306, user='admin', passwd=os.environ['DB_PW'], db='multicampus', charset='utf8')

def lambda_handler(event, context):
   
    cursor = conn.cursor()

    item = {}
    params_array = event['params']
    path_array = params_array['path']
    code_num = (path_array['code-num'])

    sql = "SELECT * FROM Stock_code WHERE Barcode='{}'"
    sql = sql.format(code_num)

    cursor.execute(sql)
    conn.commit()
    result = cursor.fetchall()
    result_list = []
    result_list = list(result[0])

    item['name'] = result_list[1]
    item['price'] = result_list[2]
    

    return {
        'statusCode': 200,
        'body': json.dumps(item,ensure_ascii=False)
    }
