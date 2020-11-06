#!/usr/bin/env python
# coding: utf-8

# # Dev workbook 1

# ## Script to copy blog posts from `posts/img` to `public/img`
# - Size for internet
# - Watermark

cd ../../../


ls


import glob
import os
import pathlib


# ### Load posts


post_folders = glob.glob("posts/img/*/*/*", recursive=True)
post_folders = [pathlib.Path(folder) for folder in post_folders]
post_folders


post_folders[0].exists()


post_folders[0]


def read_post_images(post_fp):
    with open((post_fp/"post.json"), "r") as f:
        iamge_file = f.read()
        
    

def update_public_images():
    pass




read_post_images(post_folders[0])




def read_post_images(post_fp):
    images = []
    with open((post_fp / "post.json"), "r") as f:
        post = json.loads(f.read())
        print(post['title'])
        for block in post["body"]["divs"]:
            if block["type"] == "photo":
                photo = block["file"]
                if not photo:
                    continue
                images.append(photo)
    return images



def read_posts():
    post_folders = glob.glob(POST_PATH, recursive=True)
    post_folders = [pathlib.Path(folder) for folder in post_folders]
    return post_folders


import json


POST_PATH = "posts/img/*/*/*"
PUB_PATH = "public"


post_fps = read_posts()
for fp in post_fps:
    image_files = read_post_images(fp)
    for image in image_files:
        image_fp = (fp / image)
        pub_image_fp = PUB_PATH / (pathlib.Path(*fp.split()[1:]) / image)
        print(image_fp, pub_image_fp)
#         shutil.copy(image_fp, pub_image_fp)


# post_slug = "1-joy-in-life"
post_slug = ""



import json
import glob
import os
import shutil
import pathlib

import traceback

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

POST_PATH = "posts/img/*/*/*"
PUB_PATH = "public"
MAX_PX_SIZE = 1080

def main():
#     args = parse_args()
#     post_slug = args.post_slug
    if post_slug:
        print(f"Copying single post: {post_slug}")
    else:
        print("Copying all posts")
    
    post_fps = read_posts()
    for fp in post_fps:
        if post_slug and not str(fp).endswith(post_slug):
            continue
        print(f"Processing {fp}")
        try:
            image_files = read_post_images(fp)
        except:
            print(f"Failed to read images in post: {fp}")
            print(traceback.print_exc())
            image_files = []
            
        pub_fp = PUB_PATH / (pathlib.Path(*fp.parts[1:]))
            
        post_fp = (fp / "post.json")
        pub_post_fp = (pub_fp / "post.json")
        print(f"{str(post_fp)} -> {str(pub_post_fp)}")
        pathlib.Path(*pub_post_fp.parts[:-1]).mkdir(exist_ok=True, parents=True)
        shutil.copyfile(post_fp, pub_post_fp)    

        for image in image_files:
            image_fp = (fp / image["file"])
            pub_image_fp = (pub_fp / image["file"])
            print(image_fp)
            
            image_obj = load_image(image_fp)
            image_obj = resize_pixels(image_obj, MAX_PX_SIZE)
            image_obj = add_watermark(image_obj, date=image["date"])
            
            print(f"{str(image_fp)} -> {str(pub_image_fp)}")
            write_image(image_obj, pub_image_fp)
            
    

def parse_args():
    import argparse
    parser = argparse.ArgumentParser(description="Convert images in posts to public images for website")
    parser.add_argument(
        "--post-slug",
        default="",
        help=(
            "Update a single post (skip the rest). "
            "Example slug: 4-lakota-dream-of-what-was-to-be"
        )
    )
    args = parser.parse_args()
    return args

            
def load_image(image_fp):
    image = Image.open(image_fp).convert("RGBA")
    return image
    


def add_watermark(image_obj, **kwargs):
    photo_date = kwargs["date"]
    upper_right_text = "© Alex Galea 2020"
    bottom_left_text = f"photos.alexgalea.ca"
    
    txt_obj = Image.new("RGBA", image_obj.size, (255,255,255,0))
    font = ImageFont.truetype("./fonts/PlayfairDisplay-Black.ttf", 40)
    draw = ImageDraw.Draw(txt_obj)
    w, h = image_obj.size
    draw.text((w-400, 50), upper_right_text, (255,255,255, 70), font=font)
    draw.text((50, h-100), bottom_left_text, (255,255,255, 70), font=font)
    image_obj = Image.alpha_composite(image_obj, txt_obj)
        
#     from matplotlib.pyplot import imshow
#     import numpy as np        
#     image_obj.convert('RGB').save('./dev/watermark.jpg')
#     imshow(np.asarray(image_obj), aspect='auto')
#     raise
    
    return image_obj


    

def resize_pixels(image_obj, max_px_size):
    width_0, height_0 = image_obj.size

    if max((width_0, height_0)) <= max_px_size:
        # The image is smaller than the crop size, do nothing
        return image_obj

    if width_0 > height_0:
        wpercent = max_px_size / float(width_0)
        hsize = int(float(height_0) * float(wpercent))
        img = image_obj.resize((max_px_size, hsize), Image.ANTIALIAS)
        return img
    else:
        hpercent = max_px_size / float(height_0)
        wsize = int(float(width_0) * float(hpercent))
        img = image_obj.resize((wsize, max_px_size), Image.ANTIALIAS)
        return img
            

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
                images.append({})
                images[-1]["file"] = photo
                images[-1]["date"] = post["photos_taken_date"]
    return images


def write_image(image_obj, pub_image_fp):
    image_obj.convert("RGB").save(pub_image_fp)


main()




