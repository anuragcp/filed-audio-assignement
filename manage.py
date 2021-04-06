# coding: utf-8
from flask_script import Manager
from application import create_app
import application.models as model
# Used by app debug & livereload
app = create_app()
print("app created")
manager = Manager(app)
@manager.command
def run():
    """Run app."""
    app.run()

if __name__ == "__main__":
    manager.run()