from flask import Flask, render_template, jsonify, redirect
from flask_cors import CORS

app = Flask(__name__)

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


@app.route('/button')
def button():
    return redirect('/button')


@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)


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
