from logging import ERROR, StreamHandler
import os
import sys

from flask import current_app, Flask, render_template, jsonify, request, session
import stripe


app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])

if not app.debug:
    log_handler = StreamHandler(sys.stderr)
    log_handler.setLevel(ERROR)
    app.logger.addHandler(log_handler)


@app.route('/')
def index_page():
    return render_template('index.html')


@app.route('/buy', methods=["POST"])
def buy():
    stripe.api_key = current_app.config['STRIPE_SECRET_KEY']
    request_json = request.get_json()

    token = request_json.get('token')
    extra_info = request_json.get('extra_info')

    stripe_response = stripe.Charge.create(
        amount=3000,
        currency='usd',
        description='Opolis Shirt',
        metadata=extra_info,
        card=token['id'],
        receipt_email=token['email'],
    )

    return jsonify({})

if __name__ == '__main__':
    app.run()
