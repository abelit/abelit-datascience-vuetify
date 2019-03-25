from flask import Flask, render_template, jsonify, redirect,request
from flask_cors import CORS

from config import Config
from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__)

app.config.from_object('config')
db = SQLAlchemy(app)

cors = CORS(app, resources={r"/*": {"origins": "*"}})



# 指定static的url地址使用static_url_path参数
# app = Flask(__name__,static_url_path='')


# @app.route('/')
# def index():
#     return render_template('index.html')

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return render_template("index.html")


@app.route('/ping')
def ping():
    return 'Pong!'


@app.route('/db')
def mydb():
    return "SQLALCHEMY_DATABASE_URI"


@app.route('/button')
def button():
    return redirect('/button')


@app.route('/api/login', methods=["POST"])
def login():
    name="ychenid@live.com"
    password="password"
    userdata = request.get_json()
    userdata.update({
        "name1": name,
        "password1": password
    })
    if request.method == 'POST':
        return jsonify(userdata.get('name'))

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)

@app.route('/test')
def test():
    return Config.SQLALCHEMY_DATABASE_URI


@app.route('/books', methods=['GET'])
def all_books():
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
        },
        {
            'title': 'Data Science',
            'author': 'Abelit',
            'read': True
        }
    ]
    return jsonify({
        'status': 'success',
        'books': BOOKS
    })


if __name__ == '__main__':
    app.run(debug=True)
