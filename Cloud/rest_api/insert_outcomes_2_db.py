import json
from json import dumps, loads
import pymysql
import json
import os
import time


def lambda_handler(event, context):
    conn = pymysql.connect(
        host=os.environ['DB_HOST'], port=3306, user='admin', passwd=os.environ['DB_PW'], db='multicampus', charset='utf8')

    cursor = conn.cursor()
    python_data = event  # json 파일로 변형
    
    
    sql = "INSERT INTO Error_detection(Errorimg_id,Outcome,Result_info) values('{}','{}','{}')"
    sql = sql.format("result_"+str(python_data.get("time")), python_data.get("result"), json.dumps(python_data))
    
    cursor.execute(sql)
    conn.commit()
    
    
    conn.close()
    
    print(event, type(event))
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!'),
        'result' : event
    }


