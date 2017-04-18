import os
import logging

class BaseConfig(object):
    DEBUG = False
    TESTING = False
    LOGGING_FORMAT = '%(asctime)s:%(name)s:%(levelname)s:%(message)s'
    LOGGING_LOCATION = 'app.log'
    LOGGING_LEVEL = logging.WARNING
    BR_PATH = '/br'
    BR_FOLDER = 'app/br/'

class DevelopmentConfig(BaseConfig):
    DEBUG = True
    TESTING = True
    LOGGING_LEVEL = logging.DEBUG

class ProductionConfig(BaseConfig):
    LOGGING_LEVEL = logging.INFO

config = {
        "default": "app.config.ProductionConfig",
        "dev": "app.config.DevelopmentConfig",
        }

def configure_app(app):
    mode = os.getenv('FLASK_CONFIGURATION', 'default')
    app.config.from_object(config[mode])
    app.config.from_pyfile('server.cfg',silent=True)
    handler = logging.FileHandler(app.config['LOGGING_LOCATION'])
    handler.setLevel(app.config['LOGGING_LEVEL'])
    formatter = logging.Formatter(app.config['LOGGING_FORMAT'])
    handler.setFormatter(formatter)
    app.logger.addHandler(handler)
