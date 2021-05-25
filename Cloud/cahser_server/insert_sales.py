from flask import Response, jsonify, request, render_template, redirect, url_for, make_response
from json import dumps, loads
import requests
import pymysql

import json

# json으로 값 받아온 뒤 구매 이력에 저장

item = {
    "item":
    [{
        "id": 50,
     			"Qty": 2
    },
        {
        "id": 53,
     			"Qty": 3
    },
        {
        "id": 44,
        "Qty": 5
    }]

}



item = json.dumps(item)
python_data = json.loads(item) 
items = {}

def insert_sales(item, phonenum):
<<<<<<< HEAD
    conn = pymysql.connect(
        host=os.environ['DB_HOST'], port=3306, user='admin', passwd=os.environ['DB_PW'], db='multicampus', charset='utf8')
=======
>>>>>>> 01789e33b65e3e1c701a81ad43cb75e8f71f8d89

    cursor = conn.cursor()
    sql = "INSERT INTO Sales_history(History,User_phonenum) values('{}','{}')"
    sql = sql.format((item), phonenum)

    cursor.execute(sql)
    conn.commit()
    conn.close()
    return print("query success")


insert_sales(item, '010-92222-0728')
