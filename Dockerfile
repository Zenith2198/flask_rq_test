# Use a python image as base
FROM python:3.14-slim

# Update apt and add git
RUN apt update && apt install -y git

# Add Redis
apt install -y redis-server

# Add uv
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# Copy code to container
COPY . /flask_rq_test

# Install packages into virtual environment
WORKDIR /flask_rq_test
RUN uv sync --all-groups

# Run Redis server at start
CMD ["redis-server"]