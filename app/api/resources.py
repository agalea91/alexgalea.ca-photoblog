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
from typing import List

from .security import require_auth
from . import api_rest


# class SecureResource(Resource):
#     """ Calls require_auth decorator on all requests """
#     method_decorators = [require_auth]





# EXAMPLE DATA for `post_file` variable used below:
#
# -> '/app/public/img/2020/10/1-spanish-banks/post.json'

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
    """ Get the date from the post folder path, e.g. 2020-03"""
    # TODO Should swap over the Pathlib next time I change this.
    date = "-".join(post_file.split(os.path.sep)[4:-2])
    return date

def _get_post_year(post_file) -> str:
    """ Get the dates year e.g. 03 """
    year = _get_post_date(post_file).split("-")[0]
    return year

def _get_post_month(post_file) -> str:
    """ Get the dates month e.g. 03 """
    current_app.logger.warning(post_file)
    current_app.logger.warning(_get_post_date(post_file))
    month = _get_post_date(post_file).split("-")[1]
    return month

def _get_post_name(post_file) -> str:
    """ Get post name, e.g. 1-panorama-ridge """
    name = post_file.split(os.path.sep)[-2]
    return name

def _get_url_path(post_file) -> str:
    """ Set the URL path of the post based on the path. """
    slug = os.path.join(
        *post_file.split(os.path.sep)[4:-1]
    )
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
        post_files = self._map_fs_post_files(apply_filter=True)
        posts = []
        for post_file in post_files:
            posts.append(self._get_response_data(post_file, get_neighbours=True))

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

    def _map_fs_post_files(self, apply_filter) -> list:
        if apply_filter:
            # Filter on year / month
            path_args = [
                self.year or "*",
                self.month or "*",
                self.foldername or "*",
            ]
            recur = False
            limit = self.limit

        else:
            path_args = ["**"]
            recur = True
            limit = None

        post_files_glob = (
            os.path.join(
                current_app.config["IMG_DIR"],
                *path_args,
                "post.json"
            )
        )
        # Sort most recent first
        post_files = sorted(
            glob(post_files_glob, recursive=recur),
            reverse=True
        )
        # Apply limit param
        post_files = post_files[:limit]

        current_app.logger.info(post_files)
        return post_files



    def _get_response_data(self, post_file, get_neighbours=False) -> dict:
        """ Parse post data and return dict to append to response."""
        with open(post_file, "r") as f:
            post = json.load(f)

        # Parse fields from file path / name
        post["date"] = _get_post_date(post_file)
        post["year"] = _get_post_year(post_file)
        post["month"] = _get_post_month(post_file)
        post["post_name"] = _get_post_name(post_file)
        post["url_path"] = _get_url_path(post_file)

        if get_neighbours:
            _prev_file, _next_file = self._get_neighbour_posts(post_file)
            # post["prev_date"] = _get_post_date(_prev_file)
            # post["next_date"] = _get_post_date(_next_file)

            post["prev_title"] = self._get_response_data(_prev_file, get_neighbours=False)["title"] if _prev_file else ""
            post["prev_url_path"] = _get_url_path(_prev_file) if _prev_file else ""
            post["prev_year"] = _get_post_year(_prev_file) if _prev_file else ""
            post["prev_month"] = _get_post_month(_prev_file) if _prev_file else ""
            post["prev_post_name"] = _get_post_name(_prev_file) if _prev_file else ""

            post["next_url_path"] = _get_url_path(_next_file) if _next_file else ""
            post["next_title"] = self._get_response_data(_next_file, get_neighbours=False)["title"] if _next_file else ""
            post["next_year"] = _get_post_year(_next_file) if _next_file else ""
            post["next_month"] = _get_post_month(_next_file) if _next_file else ""
            post["next_post_name"] = _get_post_name(_next_file) if _next_file else ""


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

    
    def _get_neighbour_posts(self, post_file) -> List[str]:
        all_post_files = self._map_fs_post_files(apply_filter=False)[::-1]
        size = len(all_post_files)
        _prev, _next = "", ""
        # Check edge cases
        if size == 1:
            pass
        elif size == 2:
            if post_file == all_post_files[0]:
                _prev, _next = "", all_post_files[1]
            elif post_file == all_post_files[1]:
                _prev, _next = all_post_files[0], ""
        else:
            i = 0
            for prev_file, file, next_file in zip(
                all_post_files[:-2],
                all_post_files[1:1],
                all_post_files[2:],
            ):
                i += 1
                # Check edge cases
                if i == 1:
                    if post_file == prev_file:
                        _prev = ""
                        _next = file
                        break
                elif i == size:
                    if post_file == next_file:
                        _prev = file
                        _next = ""
                        break
                
                # Main condition
                if post_file == file:
                    _prev = prev_file
                    _next = next_file

        return _prev, _next




# @api_rest.route('/secure-resource/<string:resource_id>')
# class SecureResourceOne(SecureResource):
#     """ Unsecure Resource Class: Inherit from Resource """

#     def get(self, resource_id):
#         timestamp = datetime.utcnow().isoformat()
#         return {'timestamp': timestamp}
