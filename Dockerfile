FROM python:3.12-alpine3.18

ENV PYTHONUNBUFFERED 1

COPY requirements.txt /requirements.txt

RUN apk add --no-cache --virtual .build-deps gcc libc-dev libxslt-dev && \
    apk add --no-cache libxslt
RUN apk add --upgrade --no-cache build-base linux-headers && \
    pip install --upgrade pip && \
    pip3 install -r /requirements.txt

RUN apk update && apk add --update --no-cache postgresql-client


COPY app/ /app
WORKDIR /app

RUN sed -i 's/\r$//g' entrypoint.sh
RUN chmod +x entrypoint.sh


CMD ["uwsgi", "--socket", ":9000", "--workers", "4", "--master", "--module", "config.wsgi"]
