#!/bin/bash
echo "yarn build"
yarn build
echo "python replace_dist_localhost_paths.py"
python replace_dist_localhost_paths.py
echo "s3_cloudfront_website_update.sh"
bash s3_cloudfront_website_update.sh
