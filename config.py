import os

class Config:

    LOCATION_API_BASE_URL ='https://maps.googleapis.com/maps/api/js?key=API_KEY'
    LOCATION_API_KEY = os.environ.get('LOCATION_API_KEY')
    SECRET_KEY = os.environ.get('SECRET_KEY')


class ProdConfig(Config):
    pass


class DevConfig(Config):
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}