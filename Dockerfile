FROM python:2.7-alpine

RUN pip install --no-cache-dir mongoengine celery==3.1.17 pytest pytest-cov

COPY . /opt/celerybeat-mongo/

WORKDIR /opt/celerybeat-mongo/

RUN pip install -e .

ENV C_FORCE_ROOT=1
