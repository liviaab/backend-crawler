FROM python:3.6


RUN apt-get install && apt-get -y install gcc
RUN easy_install pip

EXPOSE 3333
WORKDIR /backend-crawler
COPY . /backend-crawler

RUN pip install -r requirements.txt
CMD python3 modules/api/router.py
