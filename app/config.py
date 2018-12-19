class Development(object):
    DEBUG = True
    # # Enable protection against Cross-site Request Forgery (CSRF)
    CSRF_ENABLED = True
    SECRET_KEY = 'no-secret-key-2018!'
    SQLALCHEMY_DATABASE_URI = 'postgres://flask_user:flask@localhost:5432/flask_rest_api'


class Testing(object):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = 'postgres://user:pass@test/dbname'


class Production(object):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = 'postgres://user:pass@production/dbname'
