import sys
import os
# Insert project root path to sys.path
project_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if project_path not in sys.path:
    sys.path.insert(0, project_path)

from datetime import datetime
from application.models import db
from mongoengine.errors import ValidationError

class Songs(db.Document):
    id = db.SequenceField(primary_key = True)
    name = db.StringField(required = True, max_length = 100)
    duration = db.IntField(required = True, min_value=0)
    uploaded_on = db.DateTimeField(default = datetime.utcnow)
    # def __init__(self, *args, **kwargs):
    #     super(model.Document, self).__init__(self)
    #     try:
    #         self.name = kwargs['name']
    #         self.duration = kwargs['duration']
    #     except:
    #         print('Bad arguments for Songs')

    def clean(self):
        if self.duration < 0:
            raise ValidationError("Error : duration must be a positive value.")
