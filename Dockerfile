FROM python:3.7.1-alpine

MAINTAINER popsoften
ENV APPLICATION_ROOT /app
RUN mkdir $APPLICATION_ROOT
WORKDIR $APPLICATION_ROOT

RUN pip3 install pipenv

COPY Pipefile* $APPLICATION_ROOT/
RUN pipenv install --dev

EXPOSE 8000
