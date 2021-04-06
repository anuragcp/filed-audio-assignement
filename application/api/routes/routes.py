from flask import Blueprint, jsonify, request, json

api = Blueprint('api', __name__, url_prefix='/audio')

from application.api.controllers import audio_file


@api.route('/create', methods=['POST'])
def create():
    data = request.json
    res = audio_file.audio_file_create(data=data)
    return jsonify(res)


@api.route('/<audioFileType>/<audioFileID>', methods=['GET', 'DELETE', 'PUT'])
def handle(audioFileType,audioFileID):
    if request.method == 'DELETE':
        res = audio_file.audio_file_delete(audioFileType, int(audioFileID))
    elif request.method == 'GET':
        res = audio_file.audio_file_get(audioFileType, int(audioFileID))
    elif request.method == 'PUT':
        data = request.json
        res = audio_file.audio_file_update(audioFileType, int(audioFileID), data)
    return jsonify(res)
