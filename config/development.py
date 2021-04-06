import os
class DevelopmentConfig(object):
    """Base config class."""
    # Flask app config
    DEBUG = True
    TESTING = False
    SECRET_KEY = "qwerty"
    # Root path of project
    PROJECT_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    # Site domain
    SITE_TITLE = "title"
    SITE_DOMAIN = "http://localhost:5000"
    # MongoEngine config
    MONGODB_SETTINGS = {
        'db': 'filed_audio',
        'host': 'mongo',
        'port': 27017
    }