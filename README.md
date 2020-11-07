# Alex Galra's Photoblog


## Docker

The docker version is a WIP, but it can be started with `make run`

For now, instead get the app up and running by following the instructions in the Dockerfiles. You need to start the Flask server and the Vue app using yarn.

## Dependencies

- Yarn
- Vue Cli 3
- Python 3

## Running for development

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


## Adding a blog post

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

These are copied over to the public folder, and images are converted to internet quality and watermarked.

Do this by running:

```
python update_public_posts.py
```

