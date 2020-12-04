echo "aws s3 sync --acl public-read --sse --delete dist s3://ravenslightphoto.com"
aws s3 sync --acl public-read --sse --delete dist s3://ravenslightphoto.com
echo "aws cloudfront create-invalidation --distribution-id E28AO23RV6F4GV --paths '/*'"
aws cloudfront create-invalidation --distribution-id E28AO23RV6F4GV --paths '/*'
