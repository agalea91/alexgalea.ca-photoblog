# -*- coding: utf-8 -*-
import re
import glob

DIST_FP = "dist"

def main():
    print("Replacing 'http://localhost:8080' with 'https://ravenslightphoto.com' for *.html files")
    html_files = glob.glob(f"{DIST_FP}/**/*.html", recursive=True)

    for fp in html_files:
        replace_localhost(fp)

def replace_localhost(fp):
    with open(fp, "r") as f:
        html = f.read()

    html_ = re.sub(r'http\://localhost\:8080', 'https://ravenslightphoto.com', html)
    with open(fp, "w") as f:
        f.write(html_)


if __name__ == '__main__':
    main()
