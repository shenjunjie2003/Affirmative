class Config(object):
    SECRET_KEY = 'your-very-long-and-complex-secret-key-here'  # Replace with your actual secret key
    DEBUG = False  # Set to True if you want to enable Flask's debug mode

    # Database configuration
    MYSQL_DATABASE_USER = 'b405e5cd5117bb'
    MYSQL_DATABASE_PASSWORD = 'b22b9c56'
    MYSQL_DATABASE_DB = 'heroku_29aebe8b6ee46de'
    MYSQL_DATABASE_HOST = 'us-cluster-east-01.k8s.cleardb.net'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://b405e5cd5117bb:b22b9c56@us-cluster-east-01.k8s.cleardb.net/heroku_29aebe8b6ee46de'
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # Optional: Reduces overhead if you don't need it
    SQLALCHEMY_ENGINE_OPTIONS = {
    'pool_pre_ping': True,
    # Optional: other engine options like pool size
    'pool_size': 10,
    'max_overflow': 10,
    'pool_timeout': 30,
    'pool_recycle': 1800
    }

# dbusername = 'root'
# dbpassword = '030129happyjjday'
# dbname = 'Affirmative'