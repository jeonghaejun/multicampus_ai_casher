from flask import Flask, request, render_template

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
    return render_template("stock.html")


@app.route('/error')
def error():
    return render_template("error.html")


@app.route('/sales')
def sales():
    return render_template("sales.html")


# @app.route('/home')
# def home():
#     return 'Hello, World!'
# @app.route('/user')
# def user():
#     return 'Hello, User!'
if __name__ == '__main__':
    app.run(debug=True)
