import os

class BaseConfig(object):
    pass

class DevelopmentConfig(BaseConfig):
    BR_PATH = '/br'
    BR_FOLDER = 'app/br/'

config = {
        "default": "app.config.DevelopmentConfig",
        }

def configure_app(app):
    mode = os.getenv('FLASK_CONFIGURATION', 'default')
    app.config.from_object(config[mode])
    app.config.from_pyfile('server.cfg',silent=True)
