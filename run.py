from flask import Flask, render_template, jsonify, request
from random import *
from flask_cors import CORS
import requests

app = Flask(__name__,
            static_folder = './dist/static',
            template_folder = './dist')
cors = CORS(app, resource={r"/api/*": {"origins": "*"}})

@app.route('/api/random')
def random_number():
    response = {
        'randomNumber' : randint(1, 100)
    }
    return jsonify(response)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    # if app.debug:
        # print('in if')
    return requests.get('http://localhost:8080/{}'.format(path)).text
    # print('out')
    # return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)