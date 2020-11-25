import os
from app import app

from dotenv import load_dotenv
load_dotenv("app/.env")

class Config:
    FLASK_ENV =  os.getenv('FLASK_ENV', 'production')
    SECRET_KEY = os.getenv('FLASK_SECRET', 'danger')

    APP_DIR = os.path.dirname(__file__)
    ROOT_DIR = os.path.dirname(APP_DIR)
    DIST_DIR = os.path.join(ROOT_DIR, 'dist')

    if FLASK_ENV == "development":
        HOST = "http://localhost:8080"
    else:
        # IMG_DIR = os.path.join(DIST_DIR, "img")
        HOST = "https://ravenslightphoto.com"

    IMG_DIR = os.path.join(ROOT_DIR, "public", "img")
    # IMG_DIR = "/Users/alex/Google Drive/Photo Blog/posts/img"

    # Ignore commented out functionality below
    # IMG_IGNORE_UNDERSCORE_NAMES = True
    # IMG_IGNORE = [
    #     # "2020/09/_thunderbird",
    #     # "2020/10/_earthquake-foot",
    #     # "2020/11/_dying-of-thirst"
    # ]

    if not os.path.exists(DIST_DIR):
        raise Exception('DIST_DIR not found: {}'.format(DIST_DIR))

app.config.from_object('app.config.Config')
