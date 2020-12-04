import os
from flask import Flask, current_app, send_file

from api import api_bp
from config import Config

application = Flask(
    __name__,
    static_folder='static',
)
application.register_blueprint(api_bp)
application.logger.info(Config.FLASK_ENV)
application.config.from_object('config.Config')


# run the app.
if __name__ == "__main__":

    # Setting debug to True enables debug output. This line should be
    # removed before deploying a production app.
    # application.debug = True
    application.run()
