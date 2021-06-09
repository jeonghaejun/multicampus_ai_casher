from flask import Response, jsonify, request, render_template, redirect, url_for, make_response
from json import dumps, loads
import requests
import pymysql
import time
import json

event = {
  "result": 0,
  "item": [
    {
      "outcome": 1,
      "id": 5,
      "prob": 0.7957403659820557
    },
    {
      "outcome": 0,
      "id": 6,
      "prob": 0.7957403659820557
    },
    {
      "outcome": 1,
      "id": 7,
      "prob": 0.7957403659820557
    }
  ]
}

item = json.dumps(event)  # json 파일로 변형
python_data = json.loads(item)  # 파이썬 dict 파일로 변형

conn = pymysql.connect(
    host=os.environ['DB_HOST'], port=3306, user='admin', passwd=os.environ['DB_PW'], db='multicampus', charset='utf8')

def lambda_handler(event, context):
    cursor = conn.cursor()
    python_data = event  # json 파일로 변형
    
    sql = "INSERT INTO Error_detection(Errorimg_id,Outcome,Result_info) values('{}','{}','{}')"
    sql = sql.format(int(time.time()),python_data.get("result"),json.dumps(python_data))
    
    cursor.execute(sql)
    conn.commit()
    
    
    conn.close()
    
    print(event, type(event))
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!'),
        'result' : event
    }



