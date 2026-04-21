set -e
source .env

echo "Building docker container..."
docker build -t flask_rq_test .

docker run -t -d -p $PORT:$PORT --name flask_rq_test flask_rq_test
echo "Docker container is now running"