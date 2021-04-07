import sys
import os
# Insert project root path to sys.path
project_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if project_path not in sys.path:
    sys.path.insert(0, project_path)

from application.models.songs import Songs
from .utils import required
from mongoengine.errors import ValidationError, DoesNotExist

def create(audioFileMetadata):
    if required(data=audioFileMetadata, key_required=['name', 'duration']):
        try:
            songObj = Songs(name=audioFileMetadata['name'], duration=audioFileMetadata['duration']).save()

            if songObj is not None:
                return {'status':200, 'result': 'Success'}
        except ValidationError as e:
            return {'status': 500, 'result': f"Internal Server Error {str(e)}"}
    else:
        return {'status': 400, 'result': 'bad request: check arguments'}
        #send 500 error


def delete(audioFileID):
    try:
        document = Songs.objects(id=audioFileID)
        if len(document) == 0:
            return {'status': 400, 'result': 'bad request: file does not exists'}
        document.delete()
        return {'status': 200, 'result': 'Success'}
    except DoesNotExist as e:
        return {'status': 500, 'result': f"Internal Server Error {str(e)}"}

def update(audioFileID, audioFileMetadata):
    try:
        document = Songs.objects(id=audioFileID)
        if len(document) == 0:
            return {'status': 400, 'result': 'bad request: file does not exists'}
        document[0].update(set__name = audioFileMetadata['name'] if audioFileMetadata.get('name') is not None else document[0].name)
        document[0].update(
            set__duration=int(audioFileMetadata['duration']) if audioFileMetadata.get('duration') is not None else document[0].duration)
        return {'status': 200, 'result': 'Success'}
    except Exception as e:
        return {'status': 500, 'result':"Internal Server Error str(e)"}

def get(audioFileID):
    try:
        document = Songs.objects(id=audioFileID)
        if len(document) == 0:
            return {'status': 400, 'result': 'bad request: file does not exists'}
        print(document)
        return {
            'result': {
                'id': document[0].id,
                'name': document[0].name,
                'duration': document[0].duration,
                'uploaded_on': document[0].uploaded_on
            },
            'status': 200
        }
    except DoesNotExist as e:
        return {'status': 500, 'result': f"Internal Server Error {str(e)}"}