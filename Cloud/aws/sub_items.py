from flask import Response, jsonify, request, render_template, redirect, url_for, make_response
from json import dumps, loads
import requests
import pymysql
import json


def subtract_items(item_id, item_amounts):


    conn = pymysql.connect(
        host=os.environ['DB_HOST'], port=3306, user='admin', passwd=os.environ['DB_PW'], db='multicampus', charset='utf8')

    subtraction = "UPDATE Item_info SET Qty=Qty-{} WHERE Item_id='{}'"
    subtraction = subtraction.format(item_amounts, item_id)
    print(subtraction)
    cursor = conn.cursor()

    cursor.execute(subtraction)
    conn.commit()
    conn.close()

    return print("subtracted from stocks success")


subtract_items('0970114', 2)
