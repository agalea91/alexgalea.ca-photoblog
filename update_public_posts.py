# -*- coding: utf-8 -*-

import re
import json
import glob
import os
import sys
import shutil
import pathlib

import traceback

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

POST_PATH = "posts/img/*/*/*"
PUB_PATH = "public"
IGNORE_POSTS_STARTSWITH = "_"
WATERMARK_FONT_SIZE = 25
MAX_PX_SIZE = 1280
WATERMARK_PHOTOGRAPHER = "Alexander Galea"
WATERMARK_DOMAIN = "ravenslightphoto.com"

def main():
    args = parse_args()
    post_slug = args.post_slug
    if post_slug:
        print(f"Copying single post: {post_slug}")
    else:
        print("Refreshing all posts")

    pub_img_fp = pathlib.Path(PUB_PATH, "img")
    ans = input(f"WARNING: about to delete {str(pub_img_fp)} folder. Press enter to proceed.")
    if ans.strip() == "":
        shutil.rmtree(pub_img_fp)
    else:
        sys.exit("User exit")

    post_fps = read_posts()
    for fp in post_fps:
        if fp.parts[-1].startswith(IGNORE_POSTS_STARTSWITH):
            print(f"Ignoring {fp}")
            continue
        elif post_slug and not str(fp).endswith(post_slug):
            print(f"Ignoring {fp}")
            continue
        else:
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
    


def add_watermark(image_obj, date):
    photo_date = re.findall("\d{4}", date)[0]
    upper_right_text = f"© {WATERMARK_PHOTOGRAPHER} {photo_date}"
    bottom_left_text = f"{WATERMARK_DOMAIN}"
    
    txt_obj = Image.new("RGBA", image_obj.size, (255,255,255,0))
    font = ImageFont.truetype("./fonts/PlayfairDisplay-Black.ttf", WATERMARK_FONT_SIZE)
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
                images[-1]["date"] = post["photo"]["date_taken"]
    return images


def write_image(image_obj, pub_image_fp):
    image_obj.convert("RGB").save(pub_image_fp, optimize=True, quality=95)
    print(f"{ pathlib.Path(pub_image_fp).stat().st_size / 1e3 } kb")


if __name__ == "__main__":
    main()

