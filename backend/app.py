from logging.handlers import SMTPHandler
import logging
from flask import Flask, jsonify, request,render_template
from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token,
    jwt_refresh_token_required, create_refresh_token,
    get_jwt_identity
)
from flask_cors import CORS
import datetime
from werkzeug.security import generate_password_hash, check_password_hash

# 自定义模块
from db import db
import config
from models import User, Role, Group, Position, Menu, Tmenu



# 创建flask实例对象
app = Flask(__name__)
# 从config.py中导入配置信息
app.config.from_object(config.DevelopmentConfig)

# 导入日志配置信息
config.DevelopmentConfig.init_app(app)

db.init_app(app)

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


@app.route('/group', methods=['GET'])
def group():
    result = []
    group = Group.query.all()
    
    for g in group:
        result.append({
            "id": g.id,
            "name": g.name
        })

    return jsonify(result)


@app.route('/position', methods=['GET'])
def position():
    result = []
    position = Position.query.filter_by(status=1)

    for p in position:
        result.append({
            "id": p.id,
            "name": p.name,
        })

    return jsonify(result)

@app.route('/register', methods=['POST'])
def register():
    # 从前端Ajax请求中获取用户名
    username = request.json.get('username', None)
    name = request.json.get('name', None)
    email = request.json.get('email', None)
    password = request.json.get('password', None)
    selected_department = request.json.get('selected_department', None)
    selected_position = request.json.get('selected_position', None)
    picked_gender = request.json.get('picked_gender', None)

    # 用户注册默认状态为0即不允许登录
    status = 0
    STATUSCODE = ''
    user = User(username=username, name=name, email=email, password=generate_password_hash(
    password), group_id=selected_department, position_id=selected_position, gender=picked_gender,status=status)

    # db.session.add(user)
    # db.session.commit()
    try:
        db.session.add(user)
        db.session.commit()
        STATUSCODE = 200
    except Exception as err:
        # print(err)
        app.logger.error(err)
        STATUSCODE = 500
        
    return jsonify(STATUSCODE)

@app.route('/login', methods=['POST'])
def login():
    # 从前端Ajax请求中获取用户名
    username = request.json.get('username', None)
    password = request.json.get('password', None)

    # 获取用户信息
    user_by_name = User.query.filter_by(username=username).first()
    user_by_email = User.query.filter_by(email=username).first()

    # 组合使用用户名或邮箱进行登录
    user = user_by_name if user_by_name else user_by_email

    # 验证用户信息是否匹配
    if not user or not check_password_hash(user.password, password):
        return jsonify({"msg": "Bad username or password"}), 401

    # Use create_access_token() and create_refresh_token() to create our
    # access and refresh tokens
    access_expires = datetime.timedelta(seconds=3600)
    refresh_expires = datetime.timedelta(seconds=86400)
    ret = {
        'access_token': create_access_token(identity=user.username, expires_delta=access_expires),
        'refresh_token': create_refresh_token(identity=user.username, expires_delta=refresh_expires)
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


@app.route('/tmenu')
def tmenu():
    tm = Tmenu.query.all()
    result = []

    for i in tm:
        result.append({"id": i.id, "name": i.name,"fid": i.fid})
    
    return jsonify(result)


@app.route('/mmenu')
def mmenu():
    tm = db.engine.execute("""with RECURSIVE t(id, name, fid, depth, path, cycle) as
                           (
        select a.id, a.name, a.fid, 1, array[a.id], false from tmenu a where id=1
        union all
        select b.id, b.name, b.fid, c.depth+1, path ||b.id, b.id=any(path) from tmenu b, t c where c.id=b.fid and not cycle
    )
        select * from t
        """)
    result = []

    for i in tm:
        result.append({"id": i.id, "name": i.name, "fid": i.fid,"depth":i.depth,"path": i.path,"cycle":i.cycle})

    return jsonify(result)

if __name__ == '__main__':
    
    app.run(debug=True)
  
