import json
import logging
import os

from flask import Flask, flash, redirect, request, send_from_directory, session, url_for
from flask_cors import CORS, cross_origin
from werkzeug.utils import secure_filename


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("recipy")

app = Flask(__name__)
CORS(app, expose_headers="Authorization")


@app.route("/generate", methods=["POST"])
def generate_list():
    logger.info("Generating list.")
    print(request.data)
    response = {
        'data': 'got it!'
    }

    return response

if __name__ == "__main__":
    app.secret_key = os.urandom(24)
    app.run(debug=True, host="0.0.0.0", use_reloader=False)
