from flask import Response, jsonify, request, render_template, redirect, url_for, make_response
from json import dumps, loads
import requests
import pymysql
from __init__ import app
import json

# from .config import conn


cursor = conn.cursor()


@app.route('/items', methods=['get'])
def get_items():
    # item_id 로 db에서 name과 price 불러오기
    item_id = request.args.to_dict()

    sql = "SELECT * FROM Item_info WHERE Item_id='{}'"
    sql = sql.format(item_id["item_id"])

    cursor.execute(sql)
    conn.commit()
    result = cursor.fetchall()



    result_list = []
    result_list = list(result[0])

    parameter_dict = request.args.to_dict()

    item = {}

    item['name'] = result_list[1]
    item['price'] = result_list[2]

    return Response(dumps(item), status=200, mimetype='appplication/json')




@app.route('/delete',methods=['put'])
def deduction_items():
    item_id = request.args.to_dict()
    item_amounts = requests

    deduction = "UPDATE item_info SET Qty=Qty-{} WHERE Item_id='{}'"
    deduction = deduction.format(item_id["item_id"])

    cursor.execute(deduction)
    conn.commit()

    return Response(dumps(item), status=200, mimetype='appplication/json')
