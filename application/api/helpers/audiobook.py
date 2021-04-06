import sys
import os
# Insert project root path to sys.path
project_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if project_path not in sys.path:
    sys.path.insert(0, project_path)

from application.models.audiobook import Audiobook
from .utils import required
from mongoengine.errors import ValidationError, DoesNotExist


def create(audioFileMetadata):
    if required(data=audioFileMetadata, key_required=['title', 'author', 'narrator', 'duration']):
        try:
            audiobookObj = Audiobook(title=audioFileMetadata.get('title'),
                                     author=audioFileMetadata.get('author'),
                                     narrator=audioFileMetadata.get('narrator'),
                                     duration=audioFileMetadata.get('duration')).save()
            if audiobookObj is not None:
                return {'status': 200}
        except ValidationError as e:
            return {'status': 500, 'description': f"Internal Server Error {str(e)}"}
    else:
        return {'status': 400, 'description': 'bad request: check arguments'}
        # send 500 error


def delete(audioFileID):
    try:
        document = Audiobook.objects(id=audioFileID)
        if len(document) == 0:
            return {'status': 400, 'description': 'bad request: file does not exists'}
        document.delete()
        return {'status': 200}
    except DoesNotExist as e:
        return {'status': 500, 'description': f"Internal Server Error {str(e)}"}

def get(audioFileID):
    try:
        document = Audiobook.objects(id=audioFileID)
        if len(document) == 0:
            return {'status': 400, 'description': 'bad request: file does not exists'}
        print(document)
        return {
            'data': {
                'id': document[0].id,
                'title': document[0].title,
                'author': document[0].author,
                'narrator': document[0].narrator,
                'duration': document[0].duration,
                'uploaded_on': document[0].uploaded_on
            },
            'status': 200
        }
    except DoesNotExist as e:
        return {'status': 500, 'description': f"Internal Server Error {str(e)}"}

def update(audioFileID, audioFileMetadata):
    try:
        document = Audiobook.objects(id=audioFileID)
        if len(document) == 0:
            return {'status': 400, 'description': 'bad request: file does not exists'}
        document[0].update(set__title = audioFileMetadata['title'] if audioFileMetadata.get('title') is not None else document[0].title)
        document[0].update(
            set__duration=int(audioFileMetadata['duration']) if audioFileMetadata.get('duration') is not None else document[0].duration)
        document[0].update(
            set__author=audioFileMetadata['author'] if audioFileMetadata.get('author') is not None else
            document[0].author)
        document[0].update(
            set__narrator=audioFileMetadata['narrator'] if audioFileMetadata.get('narrator') is not None else
            document[0].narrator)
        return {'status': 200}
    except Exception as e:
        return {'status': 500, 'description':"Internal Server Error str(e)"}