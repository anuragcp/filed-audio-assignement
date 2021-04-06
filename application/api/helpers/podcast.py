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

def get(audioFileID):
    try:
        document = Podcast.objects(id=audioFileID)
        if len(document) == 0:
            return {'status': 400, 'description': 'bad request: file does not exists'}
        print(document)
        return {
            'data' :{
                'id': document[0].id,
                'name': document[0].name,
                'duration': document[0].duration,
                'host': document[0].host,
                'participants': document[0].participants,
                'uploaded_on': document[0].uploaded_on
            },
            'status': 200
        }
    except DoesNotExist as e:
        return {'status': 500, 'description': f"Internal Server Error {str(e)}"}

def update(audioFileID, audioFileMetadata):
    try:
        document = Podcast.objects(id=audioFileID)
        if len(document) == 0:
            return {'status': 400, 'description': 'bad request: file does not exists'}
        document[0].update(set__name = audioFileMetadata['name'] if audioFileMetadata.get('name') is not None else document[0].name)
        document[0].update(
            set__duration=int(audioFileMetadata['duration']) if audioFileMetadata.get('duration') is not None else document[0].duration)
        document[0].update(
            set__host=audioFileMetadata['host'] if audioFileMetadata.get('host') is not None else
            document[0].host)
        document[0].update(
            set__participants=audioFileMetadata['participants'] if audioFileMetadata.get('participants') is not None else
            document[0].participants)
        return {'status': 200}
    except Exception as e:
        return {'status': 500, 'description':"Internal Server Error str(e)"}