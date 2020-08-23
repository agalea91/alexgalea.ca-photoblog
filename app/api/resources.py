"""
REST API Resource Routing
http://flask-restplus.readthedocs.io
"""

from datetime import datetime
from flask import request, current_app
from flask_restplus import Resource
from glob import glob
import os
import json

from .security import require_auth
from . import api_rest


class SecureResource(Resource):
    """ Calls require_auth decorator on all requests """
    method_decorators = [require_auth]


@api_rest.route('/posts')
class Posts(Resource):
    """ Get full feed of posts """

    def get(self):
        timestamp = datetime.utcnow().isoformat()
        post_files_glob = (
            os.path.join(
                current_app.config['PUB_DIR'],
                "img",
                "**",
                "*.json"
            )
        )
        post_files = sorted(glob(post_files_glob, recursive=True))
        current_app.logger.warning(post_files_glob)
        current_app.logger.warning(post_files)

        posts = []
        for post_file in post_files:
            with open(post_file, "r") as f:
                posts.append(json.load(f)["desc"])

        return {'timestamp': timestamp, 'posts': posts}


@api_rest.route('/secure-resource/<string:resource_id>')
class SecureResourceOne(SecureResource):
    """ Unsecure Resource Class: Inherit from Resource """

    def get(self, resource_id):
        timestamp = datetime.utcnow().isoformat()
        return {'timestamp': timestamp}
