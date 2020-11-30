rm -r eb-app/posts
mkdir -p eb-app/posts
find public/img -name '*.json' | cpio -pdm eb-app
mv eb-app/public/img eb-app/posts/img
rm -r eb-app/public
