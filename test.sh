#!/bin/sh

set -ex

docker-compose down -v
docker-compose build
docker-compose up -d
docker-compose run debug \
    py.test -v --cov-report term-missing --cov=celerybeatmongo tests/test.py
docker-compose down -v
