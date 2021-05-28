import json

from flask import Response, jsonify, request, render_template, redirect, url_for, make_response, Flask
import requests
import pymysql
import dbModule

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")


@app.route('/login')
def login():
    return render_template("login.html")


@app.route('/stock')
def stock():
    data_db = dbModule.Database()
    sql = "SELECT * FROM Item_info"
    row = data_db.executeAll(sql)
    return render_template("stock.html", result=row)


@app.route('/error')
def error():
    data_db = dbModule.Database()
    sql = "SELECT * FROM Error_detection"
    row = data_db.executeAll(sql)
    for item in row:
        item['Errorimg_id'] = "https://yangjae-team07-bucket.s3.eu-west-2.amazonaws.com/"+ item['Errorimg_id'] + ".jpg"
    return render_template("error.html", result=row)


@app.route('/sales')
def sales():
    data_db = dbModule.Database()
    sql = "SELECT * FROM Sales_history"
    row = data_db.executeAll(sql)
    for item in row:
        item['History']= json.loads(item['History'])
    return render_template("sales.html", result=row)


# @app.route('/home')
# def home():
#     return 'Hello, World!'
# @app.route('/user')
# def user():
#     return 'Hello, User!'
if __name__ == '__main__':
    app.run(debug=True)
