# backend-crawler

This project is the backend of an application used to retrieve information of specifics lawsuits from a brazilian court of justice, TJAL.


## Run locally

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


You must have a user/role configured to run the database initializer.
If you have problems, check out [Troubleshooting & Support](https://postgresapp.com/documentation/troubleshooting.html) of Postgres.app.

Then run
```sh
$ createdb -T template0 court_crawler
$ psql court_crawler < configs/db_initializer.sql
```

If needed, change the user and password connection parameters in the configuration file located at `configs/db_credentials.ini`

Serving the API
```sh
$ python3 modules/api/router.py
```

It will open at [http://localhost:3333/](http://localhost:3333/)
