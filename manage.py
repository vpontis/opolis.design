from flask.ext.script import Manager
import os

from app import app

app.config.from_object(os.environ['APP_SETTINGS'])

manager = Manager(app)


@manager.shell
def make_shell_context():
    context = {}

    return context

if __name__ == '__main__':
    manager.run()
