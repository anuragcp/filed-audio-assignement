import sys
import os
# Insert project root path to sys.path
project_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if project_path not in sys.path:
    sys.path.insert(0, project_path)

from application.api.helpers import song, podcast, audiobook

def audio_file_create(data):
    audioFileType = data['audioFileType']
    audioFileMetadata = data['audioFileMetadata']
    if audioFileType == 'song':
        return song.create(audioFileMetadata)
    elif audioFileType == 'podcast':
        return podcast.create(audioFileMetadata)
    elif audioFileType == 'audiobook':
        return audiobook.create(audioFileMetadata)
    else:
        return {
            'status': 400,
            'description': 'Bad Request'
        }