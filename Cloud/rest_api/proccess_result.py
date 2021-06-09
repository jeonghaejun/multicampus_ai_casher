import json
from json import dumps, loads
import pymysql
import json
import os

def lambda_handler(event, context):
    conn = pymysql.connect(
        host=os.environ['DB_HOST'], port=3306, user='admin', passwd=os.environ['DB_PW'], db='multicampus', charset='utf8')
    cursor = conn.cursor()
    python_data = event  # json 파일로 변형
    
    sql = "INSERT INTO Sales_history(History,User_phonenum) values('{}','{}')"
    sql = sql.format(json.dumps(python_data), python_data["phonenum"])
    
    cursor.execute(sql)
    conn.commit()
    
    for a in range(len(python_data["item"])):
    
        item_amounts = python_data["item"][a]["Qty"]
        item_id = python_data["item"][a]["id"]
    
        subtraction = "UPDATE Item_info SET Qty=Qty-{} WHERE Item_id='{}'"
        subtraction = subtraction.format(item_amounts, item_id)
    
        
    
        cursor.execute(subtraction)
        conn.commit()
        
    
    conn.close()
    
    print(event, type(event))
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!'),
        'result' : event
    }


