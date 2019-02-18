from flask import Flask,render_template,jsonify
from flask_cors import CORS

app = Flask(__name__)

cors = CORS(app, resources={r"/*": {"origins": "*"}})

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ping')
def ping():
    return 'Pong!'

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html',name=name)


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
        }
    ]
    return jsonify({
        'status': 'success',
        'books': BOOKS
    })

if __name__ == '__main__':
    app.run(debug=True)
