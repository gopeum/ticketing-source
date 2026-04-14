#!/bin/bash

set -e

# 1. git SHA
TAG=$(git rev-parse --short HEAD)

# 2. ECR 변수
ECR=302174038725.dkr.ecr.ap-northeast-2.amazonaws.com/ticketing/event-svc

# 3. build
docker build -t event-svc:$TAG .

# 4. tag
docker tag event-svc:$TAG $ECR:$TAG

# 5. push
docker push $ECR:$TAG

# 6. 출력
echo "IMAGE_TAG=$TAG"
