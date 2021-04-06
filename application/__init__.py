# coding: utf-8
import sys
import os
# Insert project root path to sys.path
project_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if project_path not in sys.path:
    sys.path.insert(0, project_path)

from flask import Flask
from flask_wtf.csrf import CSRFProtect
from config import load_config

from application.api.routes.routes import api
from app import site
from application.models import db
from flask_mongoengine import MongoEngine

# convert python's encoding to utf8
try:
    sys.setdefaultencoding('utf8')
except (AttributeError, NameError):
    pass
def create_app():
    """Create Flask app."""
    config = load_config()
    print(f"Conguration loaded : {config}")
    app = Flask(__name__)
    app.config.from_object(config)
    if not hasattr(app, 'production'):
        app.production = not app.debug and not app.testing
    # CSRF protect
    # CSRFProtect(app)
    app.register_blueprint(api)
    app.register_blueprint(site)
    print("Blueprint registered")
    db.init_app(app)
    print('Database initialised')
    return app
