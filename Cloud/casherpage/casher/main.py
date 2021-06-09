import json

from flask import Response, jsonify, request, render_template, redirect, url_for, make_response, Flask

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    with open('abc.json', encoding='utf-8') as json_file:
        data = json.load(json_file)
        return data


if __name__ == '__main__':
    app.run(debug=True)
