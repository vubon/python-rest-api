FROM python:3

ENV PYTHONUNBUFFERED 1

RUN mkdir /code

WORKDIR /code

EXPOSE 8000

ADD requirements.txt /code/

RUN pip install -r requirements.txt

ADD . /code/