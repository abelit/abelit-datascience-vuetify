from db import db
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash


class Group(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    enname = db.Column(db.String(80), unique=True, nullable=False)
    status = db.Column(db.Integer, nullable=False)
    description = db.Column(db.Text)
    created_time = db.Column(
        db.DateTime, nullable=False, default=datetime.now)
    updated_time = db.Column(
        db.DateTime, nullable=False, default=datetime.now)


class Position(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    enname = db.Column(db.String(80), unique=True, nullable=False)
    status = db.Column(db.Integer, nullable=False)
    description = db.Column(db.Text)
    created_time = db.Column(
        db.DateTime, nullable=False, default=datetime.now)
    updated_time = db.Column(
        db.DateTime, nullable=False, default=datetime.now)


# 角色与菜单多对多关系
role_menu = db.Table('role_menu',
                     db.Column('role_id', db.Integer, db.ForeignKey(
                         'role.id'), primary_key=True),
                     db.Column('menu_id', db.Integer, db.ForeignKey(
                         'menu.id'), primary_key=True),
                     db.Column('created_time', db.DateTime,
                               nullable=False, default=datetime.now),
                     db.Column('updated_time', db.DateTime,
                               nullable=False, default=datetime.now)
                     )

# 用户与角色多对多关系
user_role = db.Table('user_role',
                     db.Column('user_id', db.Integer, db.ForeignKey(
                         'user.id'), primary_key=True),
                     db.Column('role_id', db.Integer, db.ForeignKey(
                         'role.id'), primary_key=True),
                     db.Column('created_time', db.DateTime,
                               nullable=False, default=datetime.now),
                     db.Column('updated_time', db.DateTime,
                               nullable=False, default=datetime.now)
                     )


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False, doc="user account")
    name = db.Column(db.String(80), nullable=False, doc="real username")
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    gender = db.Column(db.Integer, nullable=False, doc="1:male,0:female")
    status = db.Column(db.Integer, nullable=False, doc="0:disable,1:enable")
    group_id = db.Column(db.Integer, db.ForeignKey('group.id'), nullable=False)
    position_id = db.Column(db.Integer, db.ForeignKey(
        'position.id'), nullable=False)
    created_time = db.Column(
        db.DateTime, nullable=False, default=datetime.now)
    updated_time = db.Column(
        db.DateTime, nullable=False, default=datetime.now)
    group = db.relationship('Group',
                            backref=db.backref('users', lazy=True))
    position = db.relationship('Position',
                               backref=db.backref('users', lazy=True))
    user_role = db.relationship('Role', secondary=user_role, lazy='subquery',
                                backref=db.backref('users', lazy=True))

    def __repr__(self):
        return '<User %r>' % self.username


class Menu(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    en_name = db.Column(db.String(80), unique=True, nullable=False)
    fid = db.Column(db.Integer, nullable=False)
    url = db.Column(db.String(500), unique=True, nullable=False)
    component = db.Column(db.String(500), unique=True, nullable=False)
    icon = db.Column(db.String(50), unique=True)
    status = db.Column(db.Integer, nullable=False, doc="0:disable,1:enable")
    type = db.Column(db.Integer, nullable=False)
    order = db.Column(db.Integer, nullable=False)
    created_time = db.Column(
        db.DateTime, nullable=False, default=datetime.now)
    updated_time = db.Column(
        db.DateTime, nullable=False, default=datetime.now)


class Role(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    en_name = db.Column(db.String(80), unique=True, nullable=False)
    status = db.Column(db.Integer, nullable=False, doc="0:disable,1:enable")
    created_time = db.Column(
        db.DateTime, nullable=False, default=datetime.now)
    updated_time = db.Column(
        db.DateTime, nullable=False, default=datetime.now)
    role_menu = db.relationship('Menu', secondary=role_menu, lazy='subquery',
                                backref=db.backref('roles', lazy=True))
    user_role = db.relationship('User', secondary=user_role, lazy='subquery',
                                backref=db.backref('roles', lazy=True))


class Tmenu(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    fid = db.Column(db.Integer, nullable=False)
