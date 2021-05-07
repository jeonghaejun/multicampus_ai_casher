from flask import Response, jsonify, request, render_template, redirect, url_for, make_response
import requests
import pymysql



app = Flask(__name__)
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/index.html')
def index_2():
    return render_template("index.html")



@app.route('/login.html')
def login():
    return render_template("login.html")
# @app.route('/home')
# def home():
#     return 'Hello, World!'
# @app.route('/user')
# def user():
#     return 'Hello, User!'
if __name__ == '__main__':
    app.run(debug=True)