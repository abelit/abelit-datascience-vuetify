# 1. 数据库环境部署及使用
## 1.1 安装Postgresql数据库
```bash
apt-get install postgresql-10
sudo su - postgres
psql
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