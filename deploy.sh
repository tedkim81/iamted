#!/bin/bash

echo "🚀 Deploying to S3 (iamted.kim)..."

# S3에 파일 동기화
aws s3 sync ./static/html/ s3://iamted.kim/ \
  --profile personal \
  --acl public-read \
  --cache-control "max-age=300" \
  --exclude ".*" \
  --delete

# 배포 성공 확인
if [ $? -eq 0 ]; then
    echo "✅ Deployment complete!"
else
    echo "❌ Deployment failed!"
    exit 1
fi

