from flask import Blueprint

api = Blueprint('api', __name__, url_prefix='/audio')

@api.route('/create')
def create():
    return "<h1>wrapper to pass data to the controller</h1>"