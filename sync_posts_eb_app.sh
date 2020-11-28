rm -r eb-app/posts
find posts -name '*.json' | cpio -pdm eb-app
