import os
basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = "postgresql://postgres:password@localhost/postgres"
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
SQLALCHEMY_TRACK_MODIFICATIONS = True
BASEDIR = basedir
# 安全配置
CSRF_ENABLED = True
SECRET_KEY = 'jklklsadhfjkhwbii9/sdf\sdf'
