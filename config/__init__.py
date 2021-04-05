import sys
import os

# Insert project root path to sys.path
project_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if project_path not in sys.path:
    sys.path.insert(0, project_path)

from config.development import DevelopmentConfig
from config.default import DefaultConfig


def load_config():
    try:
        if os.environ['FLASK_ENV'] == 'developement':
            conf_object = DevelopmentConfig()
            return conf_object
    except Exception as e:
        print("INFO: [config/__init__] Using Dfault Configration.")
        conf_object = DefaultConfig()
        return conf_object
