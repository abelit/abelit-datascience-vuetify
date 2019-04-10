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