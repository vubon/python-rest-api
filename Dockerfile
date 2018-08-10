FROM python:3

ENV PYTHONUNBUFFERED 1

RUN mkdir /code2

WORKDIR /code2


ADD requirements.txt /code2/

RUN pip install -r requirements.txt

ADD . /code2/
