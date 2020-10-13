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


def _get_file_path(post_file) -> str:
    """ Parse proper file path """
    path = post_file.split(os.path.sep)[4:-1]
    path = os.path.join(
        current_app.config["HOST"],
        "img",
        *path
    )
    return path

def _get_post_date(post_file) -> str:
    """ Get the date from the post folder path."""
    # TODO Should swap over the Pathlib next time I change this.
    date = "-".join(post_file.split(os.path.sep)[4:-2])
    return date

def _get_url_path(post_file) -> str:
    """ Set the URL path of the post based on the path. """
    # TODO Should swap over the Pathlib next time I change this.
    slug = os.path.join(
        *post_file.split(os.path.sep)[4:-1]
    )
    # return os.path.join(current_app.config["HOST"], slug)
    return f"/album/{slug}"



@api_rest.route('/posts')
class Posts(Resource):
    """ Get feed of posts sorted by date in descending order.
    
    Homepage
    --------
    Use this endpoint to pull recent posts. Have a nav for
    filtering on: recent, 2020, 2019, etc... These can be pulled using
    the year parameter.
    
    Photoblog Posts Pages
    ---------------------
    If fetching data for a specific post then set include_post_content=true
    and use all file identification parameters (year, month, file).
    """

    def get(self):
        """
        GET /posts

        Parameters
        ----------
        year : str
            Photoblog year (optional).

        month : str
            Photoblog month, use with year option (optional).

        file : str
            Name of file (optional).

        limit : int
             Number of posts to return. Default is 10.

        include_post_content : str
            If set to "true", will return post content
            (text, image paths, etc..), otherwise it's dropped.
        """
        self._parse_request_args(request.args)
        post_files = self._get_json_config_files()
        posts = []
        for post_file in post_files:
            with open(post_file, "r") as f:
                post_json = json.load(f)
                posts.append(self._get_respose_data(post_json, post_file))

        current_app.logger.info("Posts:")
        current_app.logger.info(json.dumps(posts, indent=2))
        if not posts:
            current_app.logger.warning("No posts found!")

        return {'posts': posts}

    def _parse_request_args(self, args):
        current_app.logger.info("Args:")
        current_app.logger.info(json.dumps(args, indent=2))

        self.year = args.get("year", None)
        self.month = args.get("month", None)
        self.foldername = args.get("foldername", None)
        self.limit = int(args.get("limit", "10"))
        self.include_post_content = (
            True if (args.get("include_post_content", "")).lower() == "true"
            else False
        )

    def _get_json_config_files(self):

        # Filter on year / month
        path_args = [
            self.year or "*",
            self.month or "*",
            self.foldername or "*",
        ]

        post_files_glob = (
            os.path.join(
                current_app.config["IMG_DIR"],
                *path_args,
                "post.json"
            )
        )

        # Sort most recent first
        post_files = sorted(
            glob(post_files_glob), reverse=True
        )

        # Apply limit param
        post_files = post_files[:self.limit]

        current_app.logger.info(post_files_glob)
        current_app.logger.info(post_files)
        return post_files

    def _get_respose_data(self, post_json, post_file) -> dict:
        """ Parse post data and return dict to append to response."""
        post = post_json.copy()

        # Parse fields from file path / name
        post["date"] = _get_post_date(post_file)
        post["url_path"] = _get_url_path(post_file)

        # Fix image paths
        path = _get_file_path(post_file)
        post["cover_image"] = os.path.join(path, post["cover_image"])

        # Filter post content / fix image paths
        if self.include_post_content:
            for div in post["body"]["divs"]:
                if div["type"] == "photo":
                    div["file"] = os.path.join(path, div["file"])
        else:
            del post["body"]
        
        return post


# @api_rest.route('/secure-resource/<string:resource_id>')
# class SecureResourceOne(SecureResource):
#     """ Unsecure Resource Class: Inherit from Resource """

#     def get(self, resource_id):
#         timestamp = datetime.utcnow().isoformat()
#         return {'timestamp': timestamp}
