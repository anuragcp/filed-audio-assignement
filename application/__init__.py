# coding: utf-8
import sys
import os
# Insert project root path to sys.path
project_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if project_path not in sys.path:
    sys.path.insert(0, project_path)
import logging
from flask import Flask
from flask_wtf.csrf import CSRFProtect
from config import load_config
# from application.extensions import db, login_manager
# from application.models import User
# from application.controllers import user_bp

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
    CSRFProtect(app)
    # if app.debug or app.testing:
    #     # Log errors to stderr in production mode
    #     app.logger.addHandler(logging.StreamHandler())
    #     app.logger.setLevel(logging.ERROR)
    # # Register components
    # register_extensions(app)
    # register_blueprint(app)
    app.register_blueprint(api)
    app.register_blueprint(site)
    print("Blueprint registered")
    db.init_app(app)
    print('Database initialised')
    return app
# def register_extensions(app):
#     """Register models."""
#     db.init_app(app)
#     login_manager.init_app(app)
#     login_manager.login_view = 'login'
#     @login_manager.user_loader
#     def load_user(user_id):
#         return User.objects(id=user_id).first()
# def register_blueprint(app):
#     app.register_blueprint(user_bp)