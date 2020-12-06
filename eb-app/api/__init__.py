from flask import Blueprint, current_app


import werkzeug
werkzeug.cached_property = werkzeug.utils.cached_property

from flask_restplus import Api

api_bp = Blueprint(
    'api_bp',
    __name__,
    url_prefix='/api',
)
api_rest = Api(api_bp)

@api_bp.after_request
def add_header(response):
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type,Authorization'
    response.headers['Access-Control-Allow-Origin'] = 'https://ravenslightphoto.com'
    response.headers['Access-Control-Allow-Methods'] = 'OPTIONS,POST,GET'
    return response

# Register views for all resources
from api.resources import *
