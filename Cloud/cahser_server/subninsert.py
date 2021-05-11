import json
from flask import Response, jsonify, request, render_template, redirect, url_for, make_response
from json import dumps, loads
import pymysql
import json


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
item = json.dumps(item)  # json 파일로 변형
python_data = json.loads(item)  # 파이썬 dict 파일로 변형


for a in range(len(python_data["item"])):

    print(python_data["item"][a]["id"])
    print(python_data["item"][a]["Qty"])
    item_amounts = python_data["item"][a]["Qty"]
    item_id = python_data["item"][a]["id"]


    subtraction = "UPDATE Item_info SET Qty=Qty-{} WHERE Item_id='{}'"
    subtraction = subtraction.format(item_amounts, item_id)

    python_data["item"][a]

    print(subtraction)
    cursor = conn.cursor()

    cursor.execute(subtraction)
    conn.commit()
    
conn.close()


def insert_sales(item, phonenum):

    for a in range(len(python_data["item"])):

        print(python_data["item"][a])
        item = python_data["item"][a]

    item = json.dumps(item)
    cursor = conn.cursor()
    sql = "INSERT INTO Sales_history(History,User_phonenum) values('{}','{}')"
    sql = sql.format(item, phonenum)

    cursor.execute(sql)
    conn.commit()

    return print("query success")


insert_sales(item, '010-92222-0728')
