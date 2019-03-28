from flask import Flask, jsonify, request,render_template
from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token,
    jwt_refresh_token_required, create_refresh_token,
    get_jwt_identity
)

from flask_cors import CORS
import datetime

import config
from flask_sqlalchemy import SQLAlchemy

# 创建flask实例对象
app = Flask(__name__)
# 从config.py中导入配置信息
app.config.from_object(config.DevelopmentConfig)

# app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:password@localhost/dataforum"

# 创建数据库实例对象
db = SQLAlchemy(app)

from models import User

from models import Role

from models import Menu


# 跨域设置
cors = CORS(app, resources={r"/*": {"origins": "*"}})

# 设置JWT认证加密密钥
app.config['JWT_SECRET_KEY'] = 'super-secret'  # Change this!
# 创建JWT实例对象
jwt = JWTManager(app)

# 入口文件，通过入口文件跳转到vue前端
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/hello', methods=['GET'])
def hello():
    return "hello world!"

@app.route('/login', methods=['POST'])
def login():
    username = request.json.get('name', None)
    password = request.json.get('password', None)
    # 在后台打印前端提交的数据
    print(username)
    print(password)
    if (username != 'test' or password != 'test') and (username != 'abelit' or password != 'abelit'):
        return jsonify({"msg": "Bad username or password"}), 401

    # Use create_access_token() and create_refresh_token() to create our
    # access and refresh tokens
    access_expires = datetime.timedelta(seconds=3600)
    refresh_expires = datetime.timedelta(seconds=86400)
    ret = {
        'access_token': create_access_token(identity=username, expires_delta=access_expires),
        'refresh_token': create_refresh_token(identity=username, expires_delta=refresh_expires)
    }
    return jsonify(ret), 200


# The jwt_refresh_token_required decorator insures a valid refresh
# token is present in the request before calling this endpoint. We
# can use the get_jwt_identity() function to get the identity of
# the refresh token, and use the create_access_token() function again
# to make a new access token for this identity.
@app.route('/refresh', methods=['POST'])
@jwt_refresh_token_required
def refresh():
    current_user = get_jwt_identity()
    access_expires = datetime.timedelta(seconds=3600)
    ret = {
        'access_token': create_access_token(identity=current_user, expires_delta=access_expires)
    }
    return jsonify(ret), 200


@app.route('/protected', methods=['GET'])
@jwt_required
def protected():
    username = get_jwt_identity()
    return jsonify(logged_in_as=username), 200


@app.route('/menu', methods=['GET'])
@jwt_required
def menu():
    username = get_jwt_identity()
    if username == 'test':
        return jsonify({'mapdemo': '/demo/mapdemo','uidemo':'/demo/uidemo'})
    
    return jsonify({'uidemo':'/demo/uidemo'})


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


@app.route('/ping')
def ping():
    return 'Pong!'



if __name__ == '__main__':
    app.run(debug=True)
