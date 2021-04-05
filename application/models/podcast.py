import sys
import os
# Insert project root path to sys.path
project_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if project_path not in sys.path:
    sys.path.insert(0, project_path)

from application.models import Models
from datetime import datetime

model = Models.initialise()

class Podcast(model.Document):
    id = model.SequenceField(primary_key = True)
    name = model.StringField(required = True, max_length = 100)
    duration = model.IntField(required = True, min_value=0)
    host = model.StringField(required = True, max_length = 100)
    participants = model.ListField(model.StringField(max_length=100), max_length = 10)
    uploaded_on = model.DateTimeField(default = datetime.utcnow)
    # def __init__(self, **values):
    #     super(model.Document, self).__init__(self)
    #     try:
    #         self.name = values['name']
    #         self.duration = values['duration']
    #         self.host = values["host"]
    #         self.participants = values['participants']
    #     except:
    #         print('Bad arguments for User')
