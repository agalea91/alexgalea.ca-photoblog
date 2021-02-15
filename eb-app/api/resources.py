# -*- coding: utf-8 -*-
from datetime import datetime
from flask import request, current_app
from flask_restplus import Resource
from glob import glob
from copy import copy, deepcopy
import os
import re
import json
import pandas as pd
from pathlib import Path
from typing import List

from api import api_rest


# EXAMPLE DATA for `post_file` variable used below:
#
# -> '/app/public/img/2020/10/1-spanish-banks/post.json'
#
# The strategy is to match "img\/\d{4}" and cut before.

def _get_img_rel_path(post_file):
    path = re.sub(r".*\/(img\/\d{4})", r"\1", post_file)
    return path

def _get_file_path(post_file) -> str:
    """ Parse proper file path and append host """
    path = _get_img_rel_path(post_file)
    # TOOD: keep implementing line aboe  ^
    path = Path(path).parts[:-1] # Drop the file name
    path = os.path.join(
        current_app.config["HOST"],
        *path
    )
    return path

def _get_post_date(post_file) -> str:
    """ Get the date from the post folder path, e.g. 2020-03"""
    path = _get_img_rel_path(post_file)
    path_date = Path(path).parts[1:3]
    date = "-".join(path_date)
    return date

def _get_post_year(post_file) -> str:
    """ Get the dates year e.g. 03 """
    year = _get_post_date(post_file).split("-")[0]
    return year

def _get_post_month(post_file) -> str:
    """ Get the dates month e.g. 03 """
    month = _get_post_date(post_file).split("-")[1]
    return month

def _get_post_name(post_file) -> str:
    """ Get post name, e.g. 1-panorama-ridge """
    name = Path(post_file).parts[-2]
    return name

def _get_url_path(post_file) -> str:
    """ Set the URL path of the post based on the path. """
    path = _get_img_rel_path(post_file)
    slug = Path(*Path(path).parts[1:-1])
    return f"/album/{slug}"

def _validate_post_fields(post):
    # TODO: implement verification
    pass















@api_rest.route('/categories')
class Categories(Resource):
    """ Get post categories in alphabetical order.
    
    Homepage
    --------
    Use this endpoint to pull post categories for onsite search.
    """

    def get(self):
        """
        GET /categories

        Parameters
        ----------
        search_phrase : str
            Text to match.
        """
        self._parse_request_args(request.args)

        category_index = self._load_cat_indices()
        if (
            self.search_phrase is None
            or self.search_phrase.strip() == ""
        ):
            matching_cats = category_index
        else:
            matching_cats = self._lookup_categories(self.search_phrase, category_index)
            matching_cats = self._add_surrogate_keys(matching_cats)

        payload = {"categories": matching_cats}
        return payload

    def _parse_request_args(self, args):
        current_app.logger.debug("GET request args:")
        current_app.logger.debug(json.dumps(args, indent=2))

        self.search_phrase = args.get("search_phrase", None)

    @staticmethod
    def _add_surrogate_keys(records):
        _records = deepcopy(records)
        for i, record in enumerate(_records):
            record["key"] = i + 1
        return _records

    @staticmethod
    def _lookup_categories(search_phrase, category_index):
        # Clean up search phrase
        _search_phrase = search_phrase.lower().strip()

        # Vectorized lookup for speed
        df_cat = pd.DataFrame(category_index)

        # Lookup matches
        m_title_match = df_cat.name.str.lower().str.contains(_search_phrase, regex=False)
        m_desc_match = df_cat.desc.str.lower().str.contains(_search_phrase, regex=False)

        # Combine matches for each field (ANY must match -> OR logic)
        m_match = m_title_match | m_desc_match

        matching_cats = json.loads(
            df_cat[m_match]
                .sort_values("name", ascending=True)
                .to_json(orient="records")
        )
        return matching_cats

    def _load_cat_indices(self):
        cats = []
        cat_index_fp = os.path.join(
            current_app.config["IMG_DIR"],
            "categories"
        )
        with open(os.path.join(cat_index_fp, "photo.json"), "r") as f:
            photo_cats = json.load(f)
            for cat in photo_cats:
                cat["type"] = "photo"
        with open(os.path.join(cat_index_fp, "quote.json"), "r") as f:
            quote_cats = json.load(f)
            for cat in quote_cats:
                cat["type"] = "quote"

        cats = photo_cats + quote_cats

        # Dedupe
        cat_names = []
        dedupe_cats = []
        for cat in cats:
            name = cat["name"]
            if name in cat_names:
                continue
            cat_names.append(name)
            dedupe_cats.append(cat)

        return dedupe_cats








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

        tag : str
            Tag to match (optional).

        category_type

        limit : int
            Number of posts to return. Default is 10.

        include_post_content : str
            If set to "true", will return post content
            (text, image paths, etc..), otherwise it's dropped.
        """
        self._parse_request_args(request.args)
        post_files = self._map_fs_post_files(apply_filter=True)
        post_files = self._apply_post_files_limit(post_files)
        posts = []
        for post_file in post_files:
            resp_data = self._get_post_data(post_file, get_neighbours=True)
            posts.append(copy(resp_data))

        posts = self._apply_posts_tag_filter(posts)

        current_app.logger.debug("GET request posts being returned:")
        current_app.logger.debug(json.dumps(posts, indent=2))
        if not posts:
            current_app.logger.warning("No posts found!")

        payload = {"posts": posts}
        return payload

    def _parse_request_args(self, args):
        current_app.logger.debug("GET request args:")
        current_app.logger.debug(json.dumps(args, indent=2))

        self.year = args.get("year", None)
        self.month = args.get("month", None)
        self.foldername = args.get("foldername", None)
        self.tag = args.get("tag", None)
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
        else:
            path_args = ["**"]
            recur = True

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
        return post_files

    def _apply_post_files_limit(self, post_files):
        if self.tag is not None:
            return post_files
        if self.limit is None:
            return post_files
        else:
            return post_files[:self.limit]

    def _apply_posts_tag_filter(self, posts):
        if self.tag is None:
            return posts
        tag_posts = []
        for post in posts:
            if self.tag in self._get_post_tag_slugs(post, "quote"):
                tag_posts.append(post)
            elif self.tag in self._get_post_tag_slugs(post, "photo"):
                tag_posts.append(post)
        return tag_posts

    @staticmethod
    def _get_post_tag_slugs(post, tag_type):
        return [
            tag.replace(" ", "-") for tag in
            post.get(tag_type, {}).get("tags", [])
        ]

    def _get_post_data(self, post_file, get_neighbours=False) -> dict:
        """ Parse post data and return dict to append to response."""

        current_app.logger.debug(f"Opening post file: {post_file}")

        with open(post_file, "r") as f:
            post = json.load(f)

        # Check that post is valid
        _validate_post_fields(post)

        # Parse fields from file path / name
        post["date"] = _get_post_date(post_file)
        post["year"] = _get_post_year(post_file)
        post["month"] = _get_post_month(post_file)
        post["post_name"] = _get_post_name(post_file)
        post["url_path"] = _get_url_path(post_file)

        if get_neighbours:
            _prev_file, _next_file = self._get_neighbour_posts(post_file)
            # current_app.logger.debug("Found neighbors:")
            # current_app.logger.debug(_prev_file)
            # current_app.logger.debug(_next_file)
            # post["prev_date"] = _get_post_date(_prev_file)
            # post["next_date"] = _get_post_date(_next_file)

            post["prev_title"] = self._get_post_data(_prev_file, get_neighbours=False)["title"] if _prev_file else ""
            post["prev_url_path"] = _get_url_path(_prev_file) if _prev_file else ""
            post["prev_year"] = _get_post_year(_prev_file) if _prev_file else ""
            post["prev_month"] = _get_post_month(_prev_file) if _prev_file else ""
            post["prev_post_name"] = _get_post_name(_prev_file) if _prev_file else ""

            post["next_url_path"] = _get_url_path(_next_file) if _next_file else ""
            post["next_title"] = self._get_post_data(_next_file, get_neighbours=False)["title"] if _next_file else ""
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

        # Compute schema data
        if self.include_post_content:
            post["jsonld_schema"] = self._build_jsonld_schema_str(post)

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
                all_post_files[1:-1],
                all_post_files[2:],
            ):
                i += 1
                # Check edge cases
                if i == 1:
                    if post_file == prev_file:
                        _prev = ""
                        _next = file
                        break
                elif i == (size - 2):
                    if post_file == next_file:
                        _prev = file
                        _next = ""
                        break
                
                # Main condition
                if post_file == file:
                    _prev = prev_file
                    _next = next_file

        return _prev, _next

    def _build_jsonld_schema_str(self, post):
        schema = []
        for div in post["body"]["divs"]:
            if div["type"] == "photo":
                schema.append({
                    "@context": "https://schema.org/",
                    "@type": "ImageObject",
                    "contentUrl": div["file"],
                    "license": "https://creativecommons.org/licenses/by-nc/4.0/",
                    "acquireLicensePage": f"{current_app.config['HOST']}/about"
                })
        return json.dumps(schema, indent=2)







