"""
Global Flask Application Setting

See `.flaskenv` for default settings.
 """

import os
from app import app


class Config:
    # If not set fall back to production for safety
    FLASK_ENV =  os.getenv('FLASK_ENV', 'production')
    # Set FLASK_SECRET on your production Environment
    SECRET_KEY = os.getenv('FLASK_SECRET', 'Secret')

    APP_DIR = os.path.dirname(__file__)
    ROOT_DIR = os.path.dirname(APP_DIR)
    DIST_DIR = os.path.join(ROOT_DIR, 'dist')

    IMG_DIR = os.path.join(ROOT_DIR, "public", "img")
    if FLASK_ENV == "development":
        HOST = "http://localhost:8080"
    else:
        # IMG_DIR = os.path.join(DIST_DIR, "img")
        HOST = "https://photos.alexgalea.ca"

    IMG_IGNORE = [
        "2020/09/1-thunderbird",
        "2020/10/2-the-story-of-s7ayulh-thunder",
        "2020/10/3-earthquake-foot",
    ]

    if not os.path.exists(DIST_DIR):
        raise Exception(
            'DIST_DIR not found: {}'.format(DIST_DIR))

app.config.from_object('app.config.Config')
