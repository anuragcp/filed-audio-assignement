# coding: utf-8
from flask_script import Manager
from application import create_app
from flask_swagger_ui import get_swaggerui_blueprint
# Used by app debug & livereload
app = create_app()
print("app created")

### swagger specific ###
SWAGGER_URL = '/swagger'
API_URL = '/static/swagger.json'
SWAGGERUI_BLUEPRINT = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "filed-audio-assignment"
    }
)
app.register_blueprint(SWAGGERUI_BLUEPRINT, url_prefix=SWAGGER_URL)
### end swagger specific ###



manager = Manager(app)
@manager.command
def run():
    """Run app."""
    app.run()

if __name__ == "__main__":
    manager.run()