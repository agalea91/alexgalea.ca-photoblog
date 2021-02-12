# -*- coding: utf-8 -*-
import json
import shutil

print("Backing up vue.config.js")
shutil.copyfile("vue.config.js", "vue.config.js.backup")

website_urls_fp = "../../scrapy-crawler/js_crawl/crawl-data/website_urls.json"
with open(website_urls_fp, "r") as f:
    website_urls = json.loads(f.read())
website_urls = [
    url.replace("https://ravenslightphoto.com", "") for url in website_urls
]

print(f"Copying urls from {website_urls_fp} to vue.config.js")

with open("vue.config.js", "r") as f:
    vue_config_lines = f.read().splitlines()

updated_vue_config_lines = []
for line in vue_config_lines:
    if line.startswith("const prerenderRoutes"):
        updated_vue_config_lines.append(
            "const prerenderRoutes = {}".format(
                json.dumps(website_urls).replace('"', "'")
            )
        )
    else:
        updated_vue_config_lines.append(line)

with open("vue.config.js", "w") as f:
    for line in updated_vue_config_lines:
        f.write(f"{line}\n")

