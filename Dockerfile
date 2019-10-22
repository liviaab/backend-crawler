FROM python:3

COPY . /backend-crawler
WORKDIR /backend-crawler
RUN apt-get install gcc
RUN pip install -r requirements.txt
CMD ["python3", "/modules/api/router.py"]
