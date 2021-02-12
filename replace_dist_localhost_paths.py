# -*- coding: utf-8 -*-
import re
import glob

DIST_FP = "dist"

def main():
    print("Replacing 'http://localhost:8080' with 'https://ravenslightphoto.com' for *.html files")
    html_files = glob.glob(f"{DIST_FP}/**/*.html", recursive=True)

    for fp in html_files:
        replace_localhost_client(fp)

    print("Replacing 'http://localhost:5000' with 'https://api.ravenslight.com' for *.js files")
    js_files = glob.glob(f"{DIST_FP}/static/js/app.*.js")
    replace_localhost_server(js_files[0])



def replace_localhost_client(fp):
    with open(fp, "r") as f:
        html = f.read()

    html_ = re.sub(r'http\://localhost\:8080', 'https://ravenslightphoto.com', html)
    with open(fp, "w") as f:
        f.write(html_)

def replace_localhost_server(fp):
    with open(fp, "r") as f:
        js = f.read()

    js_ = re.sub(r'http\://localhost\:5000', 'https://api.ravenslightphoto.com', js)
    with open(fp, "w") as f:
        f.write(js_)

if __name__ == '__main__':
    main()
