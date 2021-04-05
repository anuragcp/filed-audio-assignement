from flask import Flask, Blueprint

site = Blueprint('site', __name__)

@site.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    site.run()
