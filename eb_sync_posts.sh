#!/bin/bash
echo "-r eb-app/posts"
rm -r eb-app/posts
echo "-p eb-app/posts"
mkdir -p eb-app/posts
echo "public/img -name '*.json' | cpio -pdm eb-app"
find public/img -name '*.json' | cpio -pdm eb-app
echo "eb-app/public/img eb-app/posts/img"
mv eb-app/public/img eb-app/posts/img
echo "-r eb-app/public"
rm -r eb-app/public
