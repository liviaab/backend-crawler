# backend-crawler

This project is the backend of an application used to retrieve information of specifics lawsuits from a brazilian court of justice, TJAL.


## Getting Started

### Running on your local machine

This project was built using `python3`, `pip3` to install the libraries and `PostgreSQL` version 11.2 or above.

Clone the repo
```sh
$ git clone https://github.com/liviaab/backend-crawler.git
$ cd backend-crawler
```

Install the requirements file:
```sh
$ pip3 install -r requirements.txt
```

You must have a user/role configured to run the database initializer. If you have problems, check out Postgres.app [Troubleshooting & Support](https://postgresapp.com/documentation/troubleshooting.html).

Then run
```sh
$ createdb -T template0 court_crawler
$ psql court_crawler < configs/db_initializer.sql
```

If needed, change the user and password connection parameters in the configuration file located at `configs/db_credentials.local`

Serving the API
```sh
$ python3 modules/api/router.py
```

It will open at [http://localhost:3333/](http://localhost:3333/)

#### Running the tests
```sh
$ pytest -s
```

You can also test with `postman` using the request URL `http://localhost:3333/api/v1/processes/<process_number>`

Process number examples:

- 0067154-55.2010.8.02.0001
- 0000575-40.2014.8.02.0081
- 0000214-28.2011.8.02.0081
- 0717561-98.2019.8.02.0001
- 0716715-81.2019.8.02.0001
- 0725703-91.2019.8.02.0001


The frontend project is [here](https://github.com/liviaab/frontend-crawler)
