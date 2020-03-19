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

g1 = Group(name='信息部',alias='IT')  
g2 = Group(name='财务部',alias='Finance') 
db.session.add_all([g1,g2])
db.session.commit()

p1 = Position(name='经理',alias='Manager')  
p2 = Position(name='主管',alias='Supervisor') 
p3 = Position(name='助理',alias='Assistant') 
db.session.add_all([p1,p2,p3])
db.session.commit()

u1 = User(name='chenying',alias='chenying',surname='陈英',email='ychenid@live.com',passwd=generate_password_hash('123'),gender=1)
u1.groups = g1
u1.positions = p3  
u2 = User(name='xiaodawei',alias='xiaodawei',surname='肖大伟',email='xiaodawei@live.com',passwd=generate_password_hash('123'),gender=1)  
u2.groups = g1
u2.positions = p2 
u3 = User(name='shinidan',alias='shinidan',surname='史尼丹',email='shinidan@live.com',passwd=generate_password_hash('123'),gender=1)  
u3.groups = g1
u3.positions = p1  
db.session.add_all([u1,u2,u3])
db.session.commit()
```
