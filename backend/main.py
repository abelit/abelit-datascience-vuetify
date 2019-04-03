# coding:utf8
from flask import Flask
from flask_jwt_extended import JWTManager
from flask_cors import CORS


# 自定义模块
from db import db
import config

from app.api.views import api as api_blueprint
from app.auth.views import auth as auth_blueprint
from app.home.views import home as home_blueprint
from app.admin.views import admin as admin_blueprint


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


# 注册自定义blueprint模块
app.register_blueprint(home_blueprint)
app.register_blueprint(admin_blueprint, url_prefix="/admin")
app.register_blueprint(auth_blueprint, url_prefix="/auth")
app.register_blueprint(api_blueprint, url_prefix="/api")


if __name__ == "__main__":
    app.run()
