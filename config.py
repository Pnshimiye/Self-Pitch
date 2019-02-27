import os


class Config:


    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI ='postgresql+psycopg2://pauline:0788812609@localhost/pitch'
    UPLOADED_PHOTOS_DEST ='app/static/photos'
    # SECRET_KEY = '<Flask WTF Secret Key>'


    #  email configurations

    MAIL_SERVER ='smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    SUBJECT_PREFIX='Pitch'
    SENDER_EMAIL='pnshimiye@gmail.com'
    
@staticmethod
def init_app(app):
    pass

class ProdConfig(Config):
    pass


class DevConfig(Config):
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}

