from decouple import config

class Config:
    SECRET_KEY=config('SECRET_KEY')
    SQLALCHEMY_QUERY_TRACKER=config('SQLALCHEMY_QUERY_TRACKER',cast=bool)

class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI=config('SQLALCHEMY_DATABASE_URI')
    SQLALCHEMY_ECHO=True
    DEBUG=True  

class ProdConfig(Config):
    pass

class TestConfig(Config):
    pass