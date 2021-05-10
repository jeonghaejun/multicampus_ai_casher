from json import dumps, loads
from botocore.vendored import requests
import pymysql
import json
from ..casher_server.config import conn
#from flask import Response


def lambda_handler(event, context):
   
    cursor = conn.cursor()

    item = {}
    params_array = event['params']
    path_array = params_array['path']
    item_no = (path_array['item-no'])

    sql = "SELECT * FROM Item_info WHERE Item_id='{}'"
    sql = sql.format(item_no)

    cursor.execute(sql)
    conn.commit()
    result = cursor.fetchall()
    result_list = []
    result_list = list(result[0])

    #parameter_dict = request.args.to_dict()

    item['name'] = result_list[1]
    item['price'] = result_list[2]
    encoding='UTF-8-sig'

    #str_return = (dumps(item), status=200, mimetype='appplication/json')

    return {
        'statusCode': 200,
        'body': json.dumps(item,ensure_ascii=False)
    }
