set -e

echo "Deleting docker container..."
docker rm --force flask_rq_test
docker rmi flask_rq_test