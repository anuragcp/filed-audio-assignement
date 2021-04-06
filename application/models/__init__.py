import sys
import os
# Insert project root path to sys.path
project_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if project_path not in sys.path:
    sys.path.insert(0, project_path)

try:
    from flask import Flask
    from flask_mongoengine import MongoEngine
    from mongoengine import connect
except ImportError:
    print("ERROR: [models/songs] while importing modules")


db = MongoEngine()