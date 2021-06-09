from flask import Response, jsonify, request, render_template, redirect, url_for, make_response
from json import dumps, loads
import requests
import pymysql
import json

# from .config import conn
conn = pymysql.connect(
    host=os.environ['DB_HOST'], port=3306, user='admin', passwd=os.environ['DB_PW'], db='multicampus', charset='utf8')

cursor = conn.cursor()
sql = " SELECT Item_id,Product_name,Price,Qty,Category FROM Item_info INTO OUTFILE 'Item_info.csv' FIELDS TERMINATED BY ',' ENCLOSED BY '"' LINES TERMINATED BY '"' "
cursor.execute(sql)

conn.commit()
conn.close()

