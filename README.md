# backend-crawler

This project is the backend of an application used to retrieve information of specifics lawsuits from a brazilian court of justice, TJAL.



## Getting Started

This project was built using `python3`, `pip3` to install the libraries and `PostgreSQL` version 10.2 or above.

Clone the repo

```sh
$ git clone https://github.com/liviaab/backend-crawler.git
$ cd backend-crawler
```


### Method 1 - Running with `docker-compose`

You will need `docker` v19.03.4 and `docker-compose` v1.24.1. The database is configured to connect to the port 5432 (postgres default port).

```sh
# build and run container
$ docker-compose up --build -d

# create tables and add seeds to database
$ docker-compose exec -T postgres psql -U postgres court_crawler < configs/db_initializer.sql
```

It will run at [http://localhost:3333/](http://localhost:3333/)

Test the [routes](#routes)


### Method 2 - From project folder

Install the requirements file:

```sh
$ pip3 install -r requirements.txt
```

You must have a user/role configured to run the database initializer. If you have problems, check out Postgres.app [Troubleshooting & Support](https://postgresapp.com/documentation/troubleshooting.html). Then run

```sh
$ createdb -T template0 court_crawler
$ psql court_crawler < configs/db_initializer.sql
```

You will probably have to change the user and password connection parameters in the configuration file located at `configs/db_credentials.local` to something like

```
host=localhost
database=court_crawler
user=[user]
password=[password]
```

And serve the API

```sh
$ python3 modules/api/router.py
```

It will run at [http://localhost:3333/](http://localhost:3333/)

Test the [routes](#routes)

### Running the tests

```sh
$ pytest -s
```


## Routes

You can test the following routes in the browser or with `postman` using the URLs

`http://localhost:3333/api/v1/courts`

`http://localhost:3333/api/v1/processes/<process_number>`


Process number examples:

- 0067154-55.2010.8.02.0001
- 0000575-40.2014.8.02.0081
- 0000214-28.2011.8.02.0081
- 0717561-98.2019.8.02.0001
- 0716715-81.2019.8.02.0001
- 0725703-91.2019.8.02.0001


The frontend project is [here](https://github.com/liviaab/frontend-crawler)
