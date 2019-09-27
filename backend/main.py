# coding:utf8
from flask import Flask, request
from flask_jwt_extended import JWTManager
from flask_cors import CORS


# 自定义模块
from db import db
import config

from app.api.views import api as api_blueprint
from app.auth.views import auth as auth_blueprint
from app.home.views import home as home_blueprint
from app.admin.views import admin as admin_blueprint


from middleware import Middleware


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
# Change this!
app.config['JWT_SECRET_KEY'] = '+\x1ba][o\x9e\x82\xa5MGsr\xa8x3\xc04\xd3\x0f\x11\x9a<z'
# 创建JWT实例对象
jwt = JWTManager(app)

# 注册中间件
# app.wsgi_app = Middleware(app.wsgi_app, request.path)

# 中间件
@app.before_request
def process_start_request():
    # print("正在访问： "+request.path)
    app.wsgi_app = Middleware(app.wsgi_app, request.path)


# @app.after_request
# def process_end_request(response):
#     print("结束访问： "+request.path)
#     return response


# 注册自定义blueprint模块
app.register_blueprint(home_blueprint)
app.register_blueprint(admin_blueprint, url_prefix="/admin")
app.register_blueprint(auth_blueprint, url_prefix="/auth")
app.register_blueprint(api_blueprint, url_prefix="/api")


if __name__ == "__main__":
    app.run()
