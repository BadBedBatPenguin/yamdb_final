## YAMDb API
![yamdb_workflow](https://github.com/BadBedBatPenguin/yamdb_final/actions/workflows/yamdb_workflow.yml/badge.svg)

YAMDb API is an online database containing reviews for different titles. Titles are divided by categories and genres. There's opportunity to comment any review. All opportunities depend on user's role. \
Used technologies: Django, Django rest framework, SimpleJWT

## How to run project

Clone repo and move to its directory:

```Shell
git clone https://github.com/BadBedBatPenguin/api_yamdb.git
```

```Shell
cd api_yamdb
```

Create and activate virtual environment:

```Shell
python3 -m venv env
```

```Shell
source env/bin/activate
```

Install packages from requirements.txt:

```Shell
python3 -m pip install --upgrade pip
```

```Shell
pip install -r requirements.txt
```

Migrate:

```Shell
python3 manage.py migrate
```

Run project:

```Shell
python3 manage.py runserver
```

## Filling database with data from csv files:
Put all necessary csv files to "api_yamdb/static/data/" \
run command:

```Shell
python3 manage.py import_csv
```

## Autors

Bahmutov Alex ([Patron322](https://github.com/Patron322)) \
Munkuev Erdem ([rdmk](https://github.com/rdmk)) \
Tsyos Max ([BadBedBatPenguin](https://github.com/BadBedBatPenguin))

