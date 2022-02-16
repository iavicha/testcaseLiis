FROM python:3.8.12-alpine
WORKDIR Users/ilia/PycharmProjects/testcaseLiis/

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install psycopg2 dependencies
RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev

RUN pip install --upgrade pip setuptools wheel
COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY . .