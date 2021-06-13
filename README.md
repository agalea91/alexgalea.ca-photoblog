# Raven's Light Photo Journal

## Project at a glance

Vue frontend with Flask API to serve images, do search, etc..

## Developing

To develop just launch the Flask API and Vue app locally:
```
./run_client.sh
./run_server.sh
```

## Production

Building for production is complicated.

 1. Crawl local dev site.   

    In order to create the sitemap and automatically fetch a list of all pages on the site, I first launch the site locally and then do a JS URL discovery crawl.

 2. Build the Vue app

    Build the site for production. At this point the site has prerendered HTML with the local API host in the strings. Run a script to fix that.

3. Upload new site

    Run an update script that uses the AWS CLI. The dist folder is synchonized with an s3 bucket. That sits behind CloudFront, and so I create an invalidation to refresh the site as well.



 ## Folders

There are three main things going on here:
| Folder | Description | Start Dev Cmd | Update Prod Cmd
| - | - | - | - |
| `src` | Vue web app. My photoblog frontend application. | `run_client.sh` | `update_client.sh`
| `eb-app` |  Newer version of flask server. Backend server providing data to the web app. ~~To be hosted on Elastic Beanstalk.~~ Only used locally for building static site. | `run_server.sh` | `update_server.sh`
~~| `app` |  Old version of flask server, to be used with docker.~~
| `posts` | Posts directory. Put new posts here and original size images. | see below |

## Quickstart

### Dependencies

- Yarn
- Vue Cli 3
- Python 3

### How to update the site

```
# Update `public` folder with `posts`
# (if adding to or editing `posts`)
update_public_posts.py

# Sync posts to flask app
./eb_sync_posts.sh

# Start dev apps
./run_server.sh
./run_client.sh

# Run crawler
cd ../../scrapy-crawler/js-crawl
source activate selenium-py36
scrapy crawl js_local_8080 -O output.json
cd -

# Copy routes to config
python update_vue_config_prerender_routes.py

# Build and upload vue app to s3
./update_client.sh

# Deploy updated server
# (if API still in use)
./update_server.sh
```

### Vue app

```
yarn install
yarn serve
```


### Eb app
Run flask server locally / test
```
./sync_posts_eb_app.sh
cd eb-app
python application.py
```



## Docker quick start

There are two apps which should both be run on the development machine:

*Flask server*
```
docker-compose build server
docker-compose run --service-ports server
```

*Vue dev server*
```
docker-compose build client
docker-compose run --service-ports client
```

## Posts

Refresh `public/img` with folders and resized, watermarked images from `posts` by running
```
python update_public_posts.py
```

Adjust global variables in `update_public_posts.py` to set image size and watermark details.

### Adding a blog post

TLDR: Add a new folder to `posts`, create a `post.json` and copy over images. Run `python update_public_postss.py` to copy changes to live dev site.

A blog post is a set of images and a `post.json` file. These are in the `posts` folder,

e.g.

```
posts
└── img
    └── 2020
        ├── 09
        │   └── 1-thunderbird
        │       ├── 20200911-IMG_7124.jpg
        │       ├── 20200911-IMG_7126.jpg
        │       ├── IMG_5959.jpg
        │       └── post.json
        └── 10
            ├── 1-joy-in-life
            │   ├── 1-20200415-IMG_5172-2.jpg
            │   ├── 2-20200415-IMG_5177.jpg
            │   ├── 3-20200415-IMG_5200.jpg
            │   ├── 4-20200415-IMG_5205.jpg
            │   └── post.json
            ├── 2-the-story-of-s7ayulh-thunder
            │   └── post.json
            ├── 3-earthquake-foot
            │   ├── 20201007-IMG_7440.jpg
            │   ├── 20201007-IMG_7508.jpg
            │   ├── post.json
            │   └── sources.txt
            └── 4-lakota-dream-of-what-was-to-be
                ├── 1-20201007-IMG_7494-2.jpg
                ├── 2-20201007-IMG_7443.jpg
                ├── 3-20201007-IMG_7503.jpg
                ├── 4-20201007-IMG_7455.jpg
                ├── IMG_6308.jpg
                └── post.json
```



