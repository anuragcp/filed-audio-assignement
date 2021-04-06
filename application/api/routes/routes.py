from flask import Blueprint, jsonify

api = Blueprint('api', __name__, url_prefix='/audio')

from application.api.controllers import audio_file

@api.route('/create')
def create():
    audioFileMetadata = {'name': 'anuragcp', 'duration':10}
    res = audio_file.song.create(audioFileMetadata=audioFileMetadata)

    return jsonify(res)

