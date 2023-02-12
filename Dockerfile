FROM python:3.22-slim-buster

ENV DEBUG=False
ENV SECRET_KEY=<DJANGO_SECRET_KEY>

ENV PYTHONUNBUFFERED 1
RUN mkdir /source
WORKDIR /source

COPY . /source/

RUN pip install -r requirements.txt