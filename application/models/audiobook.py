import sys
import os
# Insert project root path to sys.path
project_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if project_path not in sys.path:
    sys.path.insert(0, project_path)

from application.models import Models
from datetime import datetime

model = Models.initialise()

class Audiobook(model.Document):
    id = model.SequenceField(primary_key = True)
    title = model.StringField(required = True, max_length = 100)
    author = model.StringField(required=True, max_length=100)
    narrator = model.StringField(required=True, max_length=100)
    duration = model.IntField(required = True, min_value=0)
    uploaded_on = model.DateTimeField(default = datetime.utcnow)

