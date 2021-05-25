from flask import Flask, jsonify, render_template
from subprocess import call
from flask_socketio import SocketIO, send

app = Flask(__name__)
app.secret_key = "mysecret"

socket_io = SocketIO(app)


@app.route('/')
def hello_world():


    return "Hello Gaemigo Project Home Page!!"


@app.route('/chat')
def chatting():


    return render_template('index.html')


@socket_io.on("message")
def request(message):


    print("message : " + message)
    to_client = dict()
    if message == 'new_connect':
        to_client['message'] = "새로운 유저가 난입하였다!!"
        to_client['type'] = 'connect'
    else:
        to_client['message'] = message
        to_client['type'] = 'normal'
    # emit("response", {'data': message['data'], 'username': session['username']}, broadcast=True)
    send(to_client, broadcast=True)


if __name__ == '__main__':
    socket_io.run(app, debug=True, port=8080)
