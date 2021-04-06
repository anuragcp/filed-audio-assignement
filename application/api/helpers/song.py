import sys
import os
# Insert project root path to sys.path
project_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if project_path not in sys.path:
    sys.path.insert(0, project_path)

from application.models.songs import Songs
from .utils import required

def create(audioFileMetadata):
    print(f"keys = {list(audioFileMetadata.keys())}")
    if required(data=audioFileMetadata, key_list=['name', 'duration']):
        songObj = Songs(name=audioFileMetadata['name'], duration=audioFileMetadata['duration']).save()

        if songObj is not None:
            return {'status':200}
        else:
            return {'status': 400}
    else:
        return {'status': 500}
        #send 500 error

def delete():
    pass

def update():
    pass

def get():
    pass