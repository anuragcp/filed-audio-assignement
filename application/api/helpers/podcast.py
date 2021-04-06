import sys
import os
# Insert project root path to sys.path
project_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if project_path not in sys.path:
    sys.path.insert(0, project_path)

from application.models.podcast import Podcast
from .utils import required
from mongoengine.errors import ValidationError, DoesNotExist

def create(audioFileMetadata):
    if required(data=audioFileMetadata, key_required=['name', 'duration', 'host']):
        try:
            podObj = Podcast(name=audioFileMetadata.get('name'),
                             duration=audioFileMetadata.get('duration'),
                             host=audioFileMetadata.get('host'),
                             participants = audioFileMetadata.get('participants') ).save()

            if podObj is not None:
                return {'status':200}
        except ValidationError as e:
            return {'status': 500, 'description': f"Internal Server Error {str(e)}"}
    else:
        return {'status': 400, 'description': 'bad request: check arguments'}
        #send 500 error

def delete(audioFileID):
    try:
        document = Podcast.objects(id=audioFileID)
        if len(document) == 0:
            return {'status': 400, 'description': 'bad request: file does not exists'}
        document.delete()
        return {'status': 200}
    except DoesNotExist as e:
        return {'status': 500, 'description': f"Internal Server Error {str(e)}"}