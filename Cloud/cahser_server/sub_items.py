import json
from flask import Response, jsonify, request, render_template, redirect, url_for, make_response
from json import dumps, loads
import pymysql
import json

#json으로 값을 받아온 뒤 재고 table에서 값 제거

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

    item_amounts = python_data["item"][a]["Qty"]
    item_id = python_data["item"][a]["id"]

    subtraction = "UPDATE Item_info SET Qty=Qty-{} WHERE Item_id='{}'"
    subtraction = subtraction.format(item_amounts, item_id)

    python_data["item"][a]
    cursor = conn.cursor()

    cursor.execute(subtraction)
    conn.commit()

conn.close()

item = json.dumps(item)
items = {}


