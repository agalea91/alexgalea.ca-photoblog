import os
from flask import Flask, current_app, send_file

from app.api import api_bp
from app.config import Config

flask_app = Flask(__name__, static_folder='../dist/static')
flask_app.register_blueprint(api_bp)
flask_app.logger.info(Config.FLASK_ENV)

