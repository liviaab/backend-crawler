FROM python:3

RUN apt-get update && apt-get -y install gcc postgresql postgresql-contrib
RUN easy_install pip

WORKDIR /backend-crawler
COPY . /backend-crawler

RUN pip install -r requirements.txt
EXPOSE 3333
COPY . config/db_initializer.sql
RUN service postgresql start
CMD python3 modules/api/router.py
