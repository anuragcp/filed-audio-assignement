import sys
import os
# Insert project root path to sys.path
project_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if project_path not in sys.path:
    sys.path.insert(0, project_path)

from application.models.audiobook import Audiobook
from .utils import required
from mongoengine.errors import ValidationError

def create(audioFileMetadata):
    if required(data=audioFileMetadata, key_required=['title', 'author', 'narrator', 'duration']):
        try:
            audiobookObj = Audiobook(title=audioFileMetadata.get('title'),
                                     author=audioFileMetadata.get('author'),
                                     narrator=audioFileMetadata.get('narrator'),
                                     duration=audioFileMetadata.get('duration')).save()
            if audiobookObj is not None:
                return {'status':200}
        except ValidationError as e:
            return {'status': 500, 'description': f"Internal Server Error {str(e)}"}
    else:
        return {'status': 400, 'description': 'bad request: check arguments'}
        #send 500 error