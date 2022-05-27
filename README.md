## YAMDb API
![yamdb_workflow](https://github.com/BadBedBatPenguin/yamdb_final/actions/workflows/yamdb_workflow.yml/badge.svg)

YAMDb API is an online database containing reviews for different titles. Titles are divided by categories and genres. There's opportunity to comment any review. All opportunities depend on user's role. \
Used technologies: Python, Django, Django rest framework, SimpleJWT

## How to run project

Clone repo and move to its directory:

```Shell
git clone https://github.com/BadBedBatPenguin/api_yamdb.git
cd api_yamdb
```

Create and fill .env file as in sample:
```
DB_ENGINE=django.db.backends.postgresql
DB_NAME=<database_name>
POSTGRES_USER=<PostgreSQL_username>
POSTGRES_PASSWORD=<User_password>
DB_HOST=db
DB_PORT=5432
SECRET_KEY=<secret_key_from_settings.py>
ALLOWED_HOSTS='<host IPs and names separated with whitespace>'
```
Save .env file to app/infra/ directory

Start container with project:

```Shell
cd infra
docker-compose up -d --build
```

Install dependencies:

```Shell
docker-compose exec web python -m pip install --upgrade pip
docker-compose exec web pip install flake8 pep8-naming flake8-broken-line flake8-return flake8-isort
docker-compose exec web pip install -r api_yamdb/requirements.txt
```

Run tests:

```Shell
docker-compose exec web python -m flake8
docker-compose exec web pytest
```

Migrate, create superuser and collect static:
```Shell
docker-compose exec web python manage.py migrate
docker-compose exec web python manage.py createsuperuser
docker-compose exec web python manage.py collectstatic --no-input
```

Run project:

```Shell
docker-compose exec web python manage.py runserver
```

## Filling database with data from csv files:
Put all necessary csv files to "api_yamdb/static/data/" \
run command:

```Shell
python3 manage.py import_csv
```

## Running project
To look how project runs follow this link: ([YAMDB](https://51.250.98.198))
## Autors

Bahmutov Alex ([Patron322](https://github.com/Patron322)) \
Munkuev Erdem ([rdmk](https://github.com/rdmk)) \
Tsyos Max ([BadBedBatPenguin](https://github.com/BadBedBatPenguin))

