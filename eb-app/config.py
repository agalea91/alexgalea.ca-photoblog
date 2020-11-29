import os
import pathlib

from dotenv import load_dotenv
load_dotenv("app/.env")

class Config:
    FLASK_ENV =  os.getenv('FLASK_ENV', 'production')
    SECRET_KEY = os.getenv('FLASK_SECRET', 'danger')

    APP_DIR = pathlib.Path(__file__).parent.absolute()
    IMG_DIR = os.path.join(APP_DIR, "posts", "img")

    if FLASK_ENV == "development":
        HOST = "http://localhost:8080"
    else:
        # IMG_DIR = os.path.join(DIST_DIR, "img")
        HOST = "https://ravenslightphoto.com"


    # Ignore commented out functionality below
    # IMG_IGNORE_UNDERSCORE_NAMES = True
    # IMG_IGNORE = [
    #     # "2020/09/_thunderbird",
    #     # "2020/10/_earthquake-foot",
    #     # "2020/11/_dying-of-thirst"
    # ]


"""
Set app.config
"""

from app import app
app.config.from_object('app.config.Config')
