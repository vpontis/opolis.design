import os
import sys
from raven.contrib.flask import Sentry

import logging
from flask import Flask, render_template, request, session
from logging import ERROR, StreamHandler


app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])

sentry = Sentry(app, dsn=app.config['SENTRY_PRIVATE_DSN'],
                logging=not app.config['DEBUG'], level=logging.WARNING)

if not app.debug:
    log_handler = StreamHandler(sys.stderr)
    log_handler.setLevel(ERROR)
    app.logger.addHandler(log_handler)


@app.route('/')
def index_page():
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
