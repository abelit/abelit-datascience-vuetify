# 1. 数据库环境部署及使用
## 1.1 安装Postgresql数据库
```bash
$ sudo apt-get install postgresql-10
$ sudo service postgresql start/status/stop/restart
$ sudo su - postgres
$ psql
ALTER USER postgres WITH PASSWORD 'password';
pg> CREATE USER dataforum WITH PASSWORD 'password';
```

## 1.1 创建数据库

```sql
-- Database: dataforum

-- DROP DATABASE dataforum;

CREATE DATABASE dataforum
    WITH 
    OWNER = postgres
    ENCODING = 'UTF8'
    LC_COLLATE = 'Chinese (Simplified)_China.936'
    LC_CTYPE = 'Chinese (Simplified)_China.936'
    TABLESPACE = pg_default
    CONNECTION LIMIT = -1;
```

## 1.2 Postgresql递归查询

```sql
with RECURSIVE t(id,name,fid,depth,path,cycle) as
(
 select a.id,a.name,a.fid,1,array[a.id],false from tmenu a where id=1
 union all
select b.id,b.name,b.fid,c.depth+1,path||b.id,b.id=any(path) from tmenu b , t c where c.id = b.fid and not cycle
)
select * from t;
```

## 1.3 通过docker运行postgresql
#### 1) 通过docker启动postgresql实例
```bash
$ docker run --name some-postgres -e POSTGRES_PASSWORD=mysecretpassword -d postgres
```

#### 2) 通过docker启动psql
```bash
$ docker run -it --rm --network some-network postgres psql -h some-postgres -U postgres
```

#### 3) 使用docker stack deploy 或 docker-compose
```bash
# Use postgres/example user/password credentials
version: '3.1'

services:

  db:
    image: postgres
    restart: always
    environment:
      POSTGRES_PASSWORD: example

  adminer:
    image: adminer
    restart: always
    ports:
      - 8080:8080
```

```
docker stack deploy -c stack.yml postgres
```
或
```bash
docker-compose -f stack.yml up
```

## 1.4 使用manage.py管理和迁移数据库
进入Flask-sqlalchemy交互管理
```bash
python manage.py shell
```

```bash
python manage.py db init
python manage.py db migrate
python manage.py db upgrade
```

## 1.5 添加示例数据
```python
>>> from models import *
>>> g1 = Group(name='信息部',status=1)
>>> g2 = Group(name='财务部',status=1)
>>> g3 = Group(name='客关部',status=1)
>>> g4 = Group(name='营运部',status=0)
>>>
>>>
>>> db.session.add(g1)
>>> db.session.add(g2)
>>> db.session.add(g3)
>>> db.session.add(g4)
>>> db.session.commit()

>>> p1 = Position(name='员工',status=1)
>>> p2 = Position(name='主管',status=1)
>>> p3 = Position(name='经理',status=1)
>>> p4 = Position(name='总监',status=1)
>>> p5 = Position(name='总裁',status=0)
>>>
>>>
>>> db.session.add(p1)
>>> db.session.add(p2)
>>> db.session.add(p3)
>>> db.session.add(p4)
>>> db.session.add(p5)
>>> db.session.commit()
```

在模型中使用下列关系可以辅助查询
```sql
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
    password = db.Column(db.String(120), unique=True, nullable=False)
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


class Role(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    status = db.Column(db.Integer, nullable=False, doc="0:disable,1:enable")
    created_time = db.Column(
        db.DateTime, nullable=False, default=datetime.now)
    updated_time = db.Column(
        db.DateTime, nullable=False, default=datetime.now)
    role_menu = db.relationship('Menu', secondary=role_menu, lazy='subquery',
                                backref=db.backref('roles', lazy=True))
    user_role = db.relationship('User', secondary=user_role, lazy='subquery',
                                backref=db.backref('roles', lazy=True))
```
如User和Role表是多对多的关系，在模型中User类中声明"user_role = db.relationship('Role', secondary=user_role, lazy='subquery',backref=db.backref('users', lazy=True))"这句话可以实现如下查询，即找出所属某个角色的所有用户。同样，要找出某个用户所属的所有角色，需要在Role类中加入" user_role = db.relationship('User', secondary=user_role, lazy='subquery',backref=db.backref('roles', lazy=True))"。
```python
# 找出所属某个角色的所有用户
>>> from models import *
>>> r1 = Role.query.get(1)
>>> r1.users

#找出某个用户所属的所有角色
>>> u1 = User.query.get(1)
>>> u1.roles
```

## 在Flask SQLAlchemy中如何进行多对多的数据写入
```python
>>> u1 = User.query.get(1)
>>> r1 = Role.query.get(1)
>>> ur1 = user_role.insert().values(user_id=u1.id,role_id=r1.id)
>>> db.session.add(ur1)
>>> db.session.commit()

#或
>>> u2 = User.query.get(6)
>>> r2 = Role.query.get(2)
>>> u2.roles.append(r2)
>>> db.session.add(u2)
>>> db.session.commit()

#或
>>> u3 = User.query.get(6)
>>> r3 = Role.query.get(3)
>>> r3.users.append(u3)
>>> db.session.add(r3)
>>> db.session.commit()
```

# 2. Flask环境部署
```bash
#flask
#flask-cors：flask跨域
#flask-sqlalchemy: flask数据库orm
#flask-httpauth：flask的auth认证
#passlib: python密码解析库
#itsdangerous
#flask_script
#flask_migrate
#psycopg2
#psycopg2-binary

pip install flask flask-cors flask-sqlalchemy
pip install psycopg2 psycopg2-binary
pip install flask_script flask_migrate
```


# 后台错误代码及类型定义及说明


| 错误代码 | 错误说明 |
| ----- | -----  |
| 200 | 请求成功 |
| 500 | 内部错误 |
| 7** | 值存在 |


# 开发中遇到的问题与解答

## 问题1  Instance of 'scoped_session' has no 'add' member
问题示例：
```
  {
	"resource": "/d:/Workspace/Code/abelit-DataScience/backend/app/auth/views.py",
	"owner": "python",
	"code": "no-member",
	"severity": 8,
	"message": "Instance of 'scoped_session' has no 'add' member",
	"source": "pylint",
	"startLineNumber": 41,
	"startColumn": 9,
	"endLineNumber": 41,
	"endColumn": 9
}
  {
	"resource": "/d:/Workspace/Code/abelit-DataScience/backend/models.py",
	"owner": "python",
	"code": "no-member",
	"severity": 8,
	"message": "Instance of 'SQLAlchemy' has no 'Column' member",
	"source": "pylint",
	"startLineNumber": 7,
	"startColumn": 10,
	"endLineNumber": 7,
	"endColumn": 10
}
```

解决办法：
方法一：
```
pip install pylint-flask
Load the installed plugin.

For example, if you use VS code, please edit setting.json file as follows:

"python.linting.pylintArgs": ["--load-plugins", "pylint_flask"]
```
方法二：
```
pylint --generate-rcfile > pylintrc

python -m pylint --generate-rcfile > ~/.config/pylintrc

# 编辑 ~/.config/pylintrc
ignored-modules=flask_sqlalchemy

```
参考地址：https://www.youtube.com/watch?v=n9jq_lkKeUU


## 问题2
```bash
● postgresql.service - PostgreSQL database server
   Loaded: loaded (/usr/lib/systemd/system/postgresql.service; disabled; vendor>
   Active: failed (Result: exit-code) since Tue 2019-05-28 15:40:36 UTC; 4s ago
  Process: 7923 ExecStartPre=/usr/bin/postgresql-check-db-dir ${PGROOT}/data (c>

May 28 15:40:35 dataforum.org systemd[1]: Starting PostgreSQL database server...
May 28 15:40:36 dataforum.org postgres[7923]: "/var/lib/postgres/data" is missi>
May 28 15:40:36 dataforum.org postgres[7923]:   su - postgres -c "initdb --loca>
May 28 15:40:36 dataforum.org postgres[7923]: with relevant options, to initial>
May 28 15:40:36 dataforum.org systemd[1]: postgresql.service: Control process e>
May 28 15:40:36 dataforum.org systemd[1]: postgresql.service: Failed with resul>
May 28 15:40:36 dataforum.org systemd[1]: Failed to start PostgreSQL database s>

```

解决办法：
```bash
[root@dataforum ~]# su - postgres -c "initdb --locale en_US.UTF-8 -D '/var/lib/postgres/data'"
The files belonging to this database system will be owned by user "postgres".
This user must also own the server process.

The database cluster will be initialized with locale "en_US.UTF-8".
The default database encoding has accordingly been set to "UTF8".
The default text search configuration will be set to "english".

Data page checksums are disabled.

fixing permissions on existing directory /var/lib/postgres/data ... ok
creating subdirectories ... ok
selecting default max_connections ... 100
selecting default shared_buffers ... 128MB
selecting dynamic shared memory implementation ... posix
creating configuration files ... ok
running bootstrap script ... ok
performing post-bootstrap initialization ... ok
syncing data to disk ... ok

WARNING: enabling "trust" authentication for local connections
You can change this by editing pg_hba.conf or using the option -A, or
--auth-local and --auth-host, the next time you run initdb.

Success. You can now start the database server using:

    pg_ctl -D /var/lib/postgres/data -l logfile start

```