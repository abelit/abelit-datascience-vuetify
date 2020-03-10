from db import db
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash


# 用户与角色多对多关系
users_roles = db.Table('users_roles',
                       db.Column('id', db.Integer, primary_key=True),
                       db.Column('userid', db.Integer, db.ForeignKey(
                           'users.id'), primary_key=True),
                       db.Column('roleid', db.Integer, db.ForeignKey(
                           'roles.id'), primary_key=True),
                       db.Column('created_timestamp', db.DateTime,
                                 nullable=False, default=datetime.now),
                       db.Column('updated_timestamp', db.DateTime,
                                 nullable=False, default=datetime.now)
                       )

# 用户与权限多对多关系
users_permissions = db.Table('users_permissions',
                             db.Column('id', db.Integer, primary_key=True),
                             db.Column('userid', db.Integer, db.ForeignKey(
                                 'users.id'), primary_key=True),
                             db.Column('permissionid', db.Integer, db.ForeignKey(
                                 'permissions.id'), primary_key=True),
                             db.Column('created_timestamp', db.DateTime,
                                       nullable=False, default=datetime.now),
                             db.Column('updated_timestamp', db.DateTime,
                                       nullable=False, default=datetime.now)
                             )

# 用户组和角色多对多关系
groups_roles = db.Table('groups_roles',
                        db.Column('id', db.Integer, primary_key=True),
                        db.Column('groupid', db.Integer, db.ForeignKey(
                            'groups.id'), primary_key=True),
                        db.Column('roleid', db.Integer, db.ForeignKey(
                            'roles.id'), primary_key=True),
                        db.Column('created_timestamp', db.DateTime,
                                  nullable=False, default=datetime.now),
                        db.Column('updated_timestamp', db.DateTime,
                                  nullable=False, default=datetime.now)
                        )

# 用户组与权限多对多关系
groups_permissions = db.Table('groups_permissions',
                              db.Column('id', db.Integer, primary_key=True),
                              db.Column('groupid', db.Integer, db.ForeignKey(
                                  'groups.id'), primary_key=True),
                              db.Column('permissionid', db.Integer, db.ForeignKey(
                                  'permissions.id'), primary_key=True),
                              db.Column('created_timestamp', db.DateTime,
                                        nullable=False, default=datetime.now),
                              db.Column('updated_timestamp', db.DateTime,
                                        nullable=False, default=datetime.now)
                              )

# 角色与权限多对多关系
roles_permissions = db.Table('roles_permissions',
                             db.Column('id', db.Integer, primary_key=True),
                             db.Column('roleid', db.Integer, db.ForeignKey(
                                 'roles.id'), primary_key=True),
                             db.Column('permissionid', db.Integer, db.ForeignKey(
                                 'permissions.id'), primary_key=True),
                             db.Column('created_timestamp', db.DateTime,
                                       nullable=False, default=datetime.now),
                             db.Column('updated_timestamp', db.DateTime,
                                       nullable=False, default=datetime.now)
                             )

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    alias = db.Column(db.String(100))
    name = db.Column(db.String(100), unique=True,
                     nullable=False, doc="user account")
    surname = db.Column(db.String(100), nullable=False, doc="real username")
    email = db.Column(db.String(200), unique=True,
                      nullable=False, doc="user email, can login as email")
    passwd = db.Column(db.String(200), nullable=False)
    gender = db.Column(db.Integer, nullable=False, doc="1:male,0:female")
    groupid = db.Column(db.Integer, db.ForeignKey('groups.id'), nullable=False)
    positionid = db.Column(db.Integer, db.ForeignKey(
        'positions.id'), nullable=False)
    url = db.Column(db.Integer, nullable=True,
                    doc="user's home page when logined")
    autologin = db.Column(db.Integer, nullable=False,
                          default=0, doc="1:true,0:false")
    autologout = db.Column(db.Integer, default=600, nullable=False)
    lang = db.Column(db.String(10), nullable=False, default='zh_CN')
    refresh = db.Column(db.Integer, nullable=False, default=30)
    status = db.Column(db.Integer, nullable=False,
                       default=1, doc="0:disable,1:enable")
    type = db.Column(db.Integer, nullable=False, default=2,
                     doc="0:Super Admin,1:Admin,2: General,3:Guest")
    theme = db.Column(db.String(128), nullable=False, default='default')
    attempt_clock = db.Column(
        db.DateTime, nullable=False, default=datetime.now)
    attempt_failed = db.Column(db.Integer, nullable=False, default=0)
    attempt_ip = db.Column(db.String(64), nullable=False, default='')
    created_timestamp = db.Column(
        db.DateTime, nullable=False, default=datetime.now)
    updated_timestamp = db.Column(db.DateTime, nullable=False, default='')

    groups = db.relationship('Groups', backref=db.backref('users', lazy=True))
    positions = db.relationship(
        'Positions', backref=db.backref('users', lazy=True))
    users_roles = db.relationship(
        'Roles', secondary=users_roles, lazy='subquery', backref=db.backref('users', lazy=True))
    
    users_permissions = db.relationship(
        'Permissions', secondary=users_permissions, lazy='subquery', backref=db.backref('users', lazy=True))

    def __repr__(self):
        return '<Users %r>' % self.username


class Groups(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    alias = db.Column(db.String(80), unique=True, nullable=False, default='')
    status = db.Column(db.Integer, nullable=False,
                       default=1, doc="0: disable, 1: enable")
    description = db.Column(db.Text)
    created_timestamp = db.Column(
        db.DateTime, nullable=False, default=datetime.now)
    updated_timestamp = db.Column(
        db.DateTime, nullable=False, default=datetime.now)
    
    groups_roles = db.relationship(
        'Roles', secondary=groups_roles, lazy='subquery', backref=db.backref('groups', lazy=True))

    groups_permissions = db.relationship(
        'Roles', secondary=groups_permissions, lazy='subquery', backref=db.backref('groups', lazy=True))


class Positions(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    alias = db.Column(db.String(80), unique=True, nullable=False)
    status = db.Column(db.Integer, nullable=False)
    description = db.Column(db.Text)
    created_timestamp = db.Column(
        db.DateTime, nullable=False, default=datetime.now)
    updated_timestamp = db.Column(
        db.DateTime, nullable=False, default=datetime.now)




class Menus(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    alias = db.Column(db.String(80), unique=True, nullable=False)
    fid = db.Column(db.Integer, nullable=True)
    url = db.Column(db.String(500), unique=True, nullable=False)
    # component = db.Column(db.String(500), unique=True, nullable=False)
    icon = db.Column(db.String(50), unique=True)
    status = db.Column(db.Integer, nullable=False, doc="0:disable,1:enable")
    type = db.Column(db.Integer, nullable=False)
    level = db.Column(db.Integer, nullable=False)
    created_timestamp = db.Column(
        db.DateTime, nullable=False, default=datetime.now)
    updated_timestamp = db.Column(
        db.DateTime, nullable=False, default=datetime.now)


class Roles(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    alias = db.Column(db.String(80), unique=True, nullable=False)
    description = db.Column(db.Text)
    status = db.Column(db.Integer, nullable=False, doc="0:disable,1:enable")
    created_timestamp = db.Column(
        db.DateTime, nullable=False, default=datetime.now)
    updated_timestamp = db.Column(
        db.DateTime, nullable=False, default=datetime.now)
    roles_permissions = db.relationship('Permissions', secondary=roles_permissions, lazy='subquery',
                                        backref=db.backref('roles', lazy=True))
    users_roles = db.relationship('Users', secondary=users_roles, lazy='subquery',
                                  backref=db.backref('roles', lazy=True))


class Permissions(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    alias = db.Column(db.String(80), unique=True, nullable=False)
    description = db.Column(db.Text)
    status = db.Column(db.Integer, nullable=False, doc="0:disable,1:enable")
    created_timestamp = db.Column(
        db.DateTime, nullable=False, default=datetime.now)
    updated_timestamp = db.Column(
        db.DateTime, nullable=False, default=datetime.now)
    roles_permissions = db.relationship('Permissions', secondary=roles_permissions, lazy='subquery',
                                        backref=db.backref('roles', lazy=True))
    users_permissions = db.relationship('Users', secondary=users_permissions, lazy='subquery',
                                        backref=db.backref('users', lazy=True))
    groups_permissions = db.relationship('Groups', secondary=groups_permissions, lazy='subquery',
                                        backref=db.backref('groups', lazy=True))
