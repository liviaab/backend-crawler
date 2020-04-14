FROM python:3

RUN apt-get update && apt-get -y install gcc
RUN easy_install pip && pip install --upgrade pip

WORKDIR /backend-crawler
COPY . /backend-crawler

RUN pip install -r requirements.txt
