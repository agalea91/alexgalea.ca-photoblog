# -*- coding: utf-8 -*-

import json
import glob
import os
import pathlib
import shutil
import traceback

POST_PATH = "posts/img/*/*/*"
PUB_PATH = "public"

def main():
    post_fps = read_posts()
    for fp in post_fps:
        print(fp)
        try:
            image_files = read_post_images(fp)
        except:
            print(f"Failed to read images in post: {fp}")
            print(traceback.print_exc())
            
        for image_file in image_files:
            image_fp = (fp / image_file)
            pub_image_fp = PUB_PATH / (pathlib.Path(*fp.parts[1:]) / image_file)
            print(image_fp)
            image_obj = load_image(image_fp)
            
            image_obj = add_watermark(image_obj)
            image_obj = resize_pixels(image_obj)
            

            
            
            
def load_image(image_fp):
    # load and return image object
    pass


def add_watermark(image_obj):
    pass

def resize_pixels(iamge_obj):
    pass


            
            
            
#             shutil.copy(image_fp, pub_image_fp)
    

def read_posts():
    post_folders = glob.glob(POST_PATH, recursive=True)
    post_folders = [pathlib.Path(folder) for folder in post_folders]
    return post_folders

def read_post_images(post_fp):
    images = []
    with open((post_fp / "post.json"), "rb") as f:
        post = json.load(f)
        for block in post["body"]["divs"]:
            if block["type"] == "photo":
                photo = block["file"]
                if not photo:
                    continue
                images.append(photo)
    return images


