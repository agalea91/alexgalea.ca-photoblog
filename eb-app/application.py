# -*- coding: utf-8 -*-
import os
from flask import Flask, current_app, send_file

from api import api_bp
from config import Config

application = Flask(
    __name__,
    static_folder='static',
)
application.register_blueprint(api_bp)
application.config.from_object('config.Config')

flask_env = application.config["FLASK_ENV"]
application.logger.debug(f"Flask env = {flask_env}")
if flask_env == "development":
    # Enable debug logging
    application.debug = True

# run the app.
if __name__ == "__main__":

    application.run()
