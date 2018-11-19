import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') 

    UPLOADED_PHOTOS_DEST ='app/static/photos'


    #  email configurations
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://amira:marvin@localhost/pitch'




class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://amiratiffany@localhost/pitch_test'
    pass


class ProdConfig(Config):
    # SQLALCHEMY_DATABASE_URI = os.eynviron.get("DATABASE_URL")
    pass

class DevConfig(Config):
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig,
'test':TestConfig
}