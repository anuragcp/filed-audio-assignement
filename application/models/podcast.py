import sys
import os
# Insert project root path to sys.path
project_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if project_path not in sys.path:
    sys.path.insert(0, project_path)

from datetime import datetime
from application.models import db


class Podcast(db.Document):
    id = db.SequenceField(primary_key = True)
    name = db.StringField(required = True, max_length = 100)
    duration = db.IntField(required = True, min_value=0)
    host = db.StringField(required = True, max_length = 100)
    participants = db.ListField(db.StringField(max_length=100), max_length = 10)
    uploaded_on = db.DateTimeField(default = datetime.utcnow)
    # def __init__(self, **values):
    #     super(db.Document, self).__init__(self)
    #     try:
    #         self.name = values['name']
    #         self.duration = values['duration']
    #         self.host = values["host"]
    #         self.participants = values['participants']
    #     except:
    #         print('Bad arguments for Podcast')
