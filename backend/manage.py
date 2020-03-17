# coding=utf-8
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

from main import app, db

migrate = Migrate(app, db)
manager = Manager(app)

# 添加数据库迁移命令
manager.add_command('db', MigrateCommand)


@manager.option("-n","--name",dest="name", default="www.baidu.com")
def hello(name):
    print("hello world!")
    print(name)

@manager.option("-n", "--name", dest="name", default="www.baidu.com")
def world(name):
    print("haha")


if __name__ == '__main__':
    manager.run()
