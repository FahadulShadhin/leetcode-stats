# syntax=docker/dockerfile:1

# Visit the Dockerfile reference guide at
# https://docs.docker.com/go/dockerfile-reference/

ARG PYTHON_VERSION=3.10.7
FROM python:${PYTHON_VERSION}

WORKDIR /app

# Copy the source code into the container.
COPY . /app

# Install dependencies
RUN pip3 install -r requirements.txt

# Expose the port that the application listens on.
EXPOSE 8000

# Run the application.
CMD uvicorn main:app --host=0.0.0.0 --port=8000
