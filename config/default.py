# coding: utf-8
import os
class DefaultConfig(object):
    """Base config class."""
    # Flask app config
    DEBUG = True
    TESTING = False
    SECRET_KEY = "your_key"
    # Root path of project
    PROJECT_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    # Site domain
    SITE_TITLE = "title"
    SITE_DOMAIN = "http://localhost:8080"
    # MongoEngine config
    MONGODB_SETTINGS = {
        'db': 'filed_audio',
        'host': 'localhost',
        'port': 27017
    }