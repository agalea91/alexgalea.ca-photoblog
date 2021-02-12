# Raven's Light Photo Journal

## Project at a glance

There are three main things going on here:
| Folder | Description |
| - | - |
| `src` | Vue web app. My photoblog frontend application.
| `eb-app` |  Newer version of flask server. Backend server providing data to the web app. ~~To be hosted on Elastic Beanstalk.~~ Only used locally for building static site.
~~| `app` |  Old version of flask server, to be used with docker.~~
| `posts` | Posts directory. Put new posts here and original size images.

## Quickstart

### Dependencies

- Yarn
- Vue Cli 3
- Python 3

### How to update the site

```
# Sync posts to flask app
./eb_sync_posts.sh

# Run crawler
cd ../../scrapy-crawlers/js_crawl
source activate selenium-py36
scrapy crawl js_local_8080 -O output.json

# Copy routes to config
python update_vue_config_prerender_routes.py

# Build and upload vue app to s3
python update_client.sh
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

## Running for development without Docker

### Quickstart

```
# Start the server
./run_server.sh

# ** Open a new window

# Start the client
./run_client.sh

# ** open http://localhost:8080/
```

### Vue
```
yarn install
yarn serve
```


### Flask
```
pip install -r requirements.txt
flask", "run", "--host", "0.0.0.0
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
