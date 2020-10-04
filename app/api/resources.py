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
from copy import copy

from .security import require_auth
from . import api_rest


# class SecureResource(Resource):
#     """ Calls require_auth decorator on all requests """
#     method_decorators = [require_auth]


@api_rest.route('/posts')
class Posts(Resource):
    """ Get full feed of posts """

    def get(self):
        """
        GET /posts

        Parameters
        ----------
        year : str
            Photoblog year.

        month : str
            Photoblog month.

        file : str
            Name of file.
        """

        post_files = self._get_json_config_files(args=request.args)
        posts = []
        for post_file in post_files:
            with open(post_file, "r") as f:
                post = json.load(f)
                post = self._set_file_paths(post, post_file)
                posts.append(post)

        current_app.logger.info(json.dumps(posts, indent=2))

        timestamp = datetime.utcnow().isoformat()
        return {'timestamp': timestamp, 'posts': posts}


    def _get_json_config_files(self, args):
        current_app.logger.info("Finding folder with args = {}".format(dict(args)))
        year = args.get("year", None)
        month = args.get("month", None)
        filename = args.get("file", "*")

        if year is None or month is None:
            path_args = ("**",)
        else:
            path_args = (year, month.zfill(2))

        post_files_glob = (
            os.path.join(
                current_app.config["IMG_DIR"],
                *path_args,
                "{}.json".format(filename),
            )
        )
        post_files = sorted(glob(post_files_glob, recursive=True))
        current_app.logger.info(post_files_glob)
        current_app.logger.info(post_files)
        return post_files

    def _set_file_paths(self, post, post_file) -> dict:
        path = self._get_file_path(post_file)

        _post = post.copy()
        _post["date"] = self._get_post_date(post_file)
        _post["url_path"] = self._get_url_path(post_file)
        for div in _post["divs"]:
            if div["type"] == "photo":
                div["file"] = os.path.join(path, div["file"])

        _post["cover_image"] = os.path.join(path, post["cover_image"])

        return _post

    def _get_file_path(self, post_file) -> str:
        """ Parse proper file path """
        path = post_file.split(os.path.sep)[4:-1]
        path = os.path.join(
            current_app.config["HOST"],
            "img",
            *path
        )
        return path

    def _get_post_date(self, post_file) -> str:
        """ Get the date from the post folder path."""
        date = "-".join(post_file.split(os.path.sep)[4:-2])
        return date



    def _get_url_path(self, post_file) -> str:
        slug = os.path.join(
            *post_file.split(os.path.sep)[4:-1]
        )
        # return os.path.join(current_app.config["HOST"], slug)
        return f"/album/{slug}"


# @api_rest.route('/secure-resource/<string:resource_id>')
# class SecureResourceOne(SecureResource):
#     """ Unsecure Resource Class: Inherit from Resource """

#     def get(self, resource_id):
#         timestamp = datetime.utcnow().isoformat()
#         return {'timestamp': timestamp}
