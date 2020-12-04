#!/bin/bash
echo "yarn build"
yarn build
echo "s3_cloudfront_website_update.sh"
bash s3_cloudfront_website_update.sh
