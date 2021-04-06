from flask import Blueprint, jsonify, request, make_response

api = Blueprint('api', __name__, url_prefix='/audio')

from application.api.controllers import audio_file


@api.route('/create', methods=['POST'])
def create():
    data = request.json
    res = audio_file.audio_file_create(data=data)
    return make_response(jsonify(res['result']), res['status'])


@api.route('/<audioFileType>/<audioFileID>', methods=['GET', 'DELETE', 'PUT'])
def handle(audioFileType,audioFileID):
    if request.method == 'DELETE':
        res = audio_file.audio_file_delete(audioFileType, int(audioFileID))
    elif request.method == 'GET':
        res = audio_file.audio_file_get(audioFileType, int(audioFileID))
    elif request.method == 'PUT':
        data = request.json
        res = audio_file.audio_file_update(audioFileType, int(audioFileID), data)
    else:
        res = {'result': "Bad Request", 'status':400}
        return make_response(jsonify(res['result']), res['status'])
    return make_response(jsonify(res['result']), res['status'])
