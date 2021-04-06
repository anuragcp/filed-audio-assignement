from flask import Blueprint, jsonify, request, json

api = Blueprint('api', __name__, url_prefix='/audio')

from application.api.controllers import audio_file


@api.route('/create', methods=['POST'])
def create():
    data = request.json
    res = audio_file.audio_file_create(data=data)
    return jsonify(res)


@api.route('/<audioFileType>/<audioFileID>')
def delete(audioFileType,audioFileID):
    audioFileMetadata = {'name': 'anuragcp', 'duration': 10}
    res = audio_file.song.delete()
    return jsonify(res)
