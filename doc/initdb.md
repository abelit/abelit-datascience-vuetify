# Drop All database's tables
```
python3 manage.py shell

from models import *
from db import db
db.drop_all() 
```

# 创建表
```
python3 manage.py db init

python3 manage.py db migrate

python3 manage.py db upgrade
```

# 插入测试数据
```python
python3 manage.py shell

from models import *
from db import db
from werkzeug.security import generate_password_hash, check_password_hash

g1 = Group(name='超级管理员组',alias='Super Admin')  
g2 = Group(name='管理员组',alias='Admin') 
g3 = Group(name='匿名用户组',alias='Anonymous') 
db.session.add_all([g1,g2,g3])
db.session.commit()

p1 = Position(name='超级管理员',alias='Super Admin')  
p2 = Position(name='管理员',alias='Admin') 
p3 = Position(name='匿名用户',alias='Anonymous') 
db.session.add_all([p1,p2,p3])
db.session.commit()

u1 = User(name='superadmin',alias='superadmin',surname='超级管理员',email='superadmin@live.com',passwd=generate_password_hash('superadmin'),gender=1)
u1.groups = g1
u1.positions = p1 
u2 = User(name='admin',alias='admin',surname='管理员',email='admin@live.com',passwd=generate_password_hash('superadmin'),gender=1)  
u2.groups = g2
u2.positions = p2 
u3 = User(name='anonymous',alias='anonymous',surname='匿名用户',email='anonymous@live.com',passwd=generate_password_hash('anonymous'),gender=1)  
u3.groups = g3
u3.positions = p3 
db.session.add_all([u1,u2,u3])
db.session.commit()


g10 = Group(name='信息部',alias='IT')  
g11 = Group(name='财务部',alias='Finance') 
db.session.add_all([g10,g11])
db.session.commit()

p10 = Position(name='经理',alias='Manager')  
p11 = Position(name='主管',alias='Supervisor') 
p12 = Position(name='助理',alias='Assistant') 
db.session.add_all([p10,p11,p12])
db.session.commit()

u10 = User(name='chenying',alias='chenying',surname='陈英',email='ychenid@live.com',passwd=generate_password_hash('123'),gender=1)
u10.groups = g10
u10.positions = p12  
u11 = User(name='xiaodawei',alias='xiaodawei',surname='肖大伟',email='xiaodawei@live.com',passwd=generate_password_hash('123'),gender=1)  
u11.groups = g10
u11.positions = p11 
u12 = User(name='shinidan',alias='shinidan',surname='史尼丹',email='shinidan@live.com',passwd=generate_password_hash('123'),gender=1)  
u12.groups = g10
u12.positions = p10  
db.session.add_all([u10,u11,u12])
db.session.commit()
```
