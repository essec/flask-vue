from flask import Flask, render_template, jsonify, request
from flask_cors import CORS
from flask_mongoengine import MongoEngine, Document
from flask_wtf import FlaskForm
from wtforms import StringField, Form, fields
from wtforms.validators import Length
from random import randint
import requests, json

db = MongoEngine()
app = Flask(__name__,
            static_folder = './dist/static',
            template_folder = './dist')

app.config['SECRET_KEY'] = '<---YOUR_SECRET_FORM_KEY--->'
app.config['MONGODB_SETTINGS'] = {
    'db' : 'BookDB'
}

db.init_app(app)
cors = CORS(app, resource={"/api/*": {"origins": "*"}})

# class Books(db.Document):
#     meta = {'collection' : 'Book'}
#     title = db.StringField(max_length=120)
#     author = db.StringField(max_length=50)

class BookForm(FlaskForm):
    title = StringField('Title', validators=[Length(max=120)])
    author = StringField('Author', validators=[Length(max=50)])

BOOKS = [
    {
        'title': 'On the Road',
        'author': 'Jack Kerouac',
        'read': True
    },
    {
        'title': 'Harry Potter and the Philosopher\'s Stone',
        'author': 'J. K. Rowling',
        'read': False
    },
    {
        'title': 'Green Eggs and Ham',
        'author': 'Dr. Seuss',
        'read': True
    }
]

@app.route('/api/random')
def random_number():
    response = {
        'randomNumber' : randint(1, 100)
    }
    return jsonify(response)

@app.route('/api/books', methods=['GET', 'POST'])
def all_books():
    result =  {'status': 'success'}
    if request.method == 'POST':
        post_data = request.get_json()
        BOOKS.append({
            'title': post_data.get('title'),
            'author': post_data.get('author'),
            'read': post_data.get('read')
        })
        result['message'] = 'Book added!'
    else:
        result['books'] = BOOKS
    return jsonify(result)

@app.route('/api/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    # if app.debug:
        # return requests.get('http://localhost:8080/{}'.format(path)).text
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)