import csv
import os
from typing import List

from django.core.management import BaseCommand, CommandError
from django.shortcuts import get_object_or_404
from reviews import models

from api_yamdb.settings import BASE_DIR

CSV_FILES = [
    ['users.csv', models.User],
    ['category.csv', models.Category],
    ['genre.csv', models.Genre],
    ['titles.csv', models.Title],
    ['review.csv', models.Review],
    ['comments.csv', models.Comment],
]
FOREIGN_FIELD_NAMES = {
    'review': models.Review,
    'author': models.User,
    'title': models.Title,
    'genre': models.Genre,
    'category': models.Category,
}


def check_fields(fields_name: List[str], model_fields: List[str]):
    for i, _ in enumerate(fields_name):
        fields_name[i] = fields_name[i].lower()
        fields_name[i] = fields_name[i].replace('_id', '')
        if not fields_name[i] in model_fields:
            raise CommandError(
                f"{fields_name[i]} field doesn't exist "
                "in {Model} Model"
            )


def save_model(model, row, fields_name):
    try:
        obj = model()
        for i, field in enumerate(row):
            if fields_name[i] in FOREIGN_FIELD_NAMES.keys():
                foreign_model = FOREIGN_FIELD_NAMES[fields_name[i]]
                field = get_object_or_404(foreign_model, id=field)
            setattr(obj, fields_name[i], field)
        obj.save()
    except Exception as e:
        raise CommandError(e)


def process_file(csv_file, model):
    path = os.path.join(BASE_DIR, f'static/data/{csv_file}')
    model_fields = [f.name for f in model._meta.fields]
    fields_name = []
    with open(path, 'rt', encoding="utf8") as f:
        reader = csv.reader(f, dialect='excel')
        fields_name = next(reader)
        check_fields(fields_name, model_fields)
        for row in reader:
            save_model(model, row, fields_name)


def process_genre_title():
    with open(
        os.path.join(BASE_DIR, 'static/data/genre_title.csv'),
        'rt',
        encoding="utf8"
    ) as f:
        reader = csv.reader(f, dialect='excel')
        next(reader)
        for row in reader:
            try:
                title = get_object_or_404(models.Title, id=int(row[1]))
                genre = get_object_or_404(models.Genre, id=int(row[2]))
                title.genre.add(genre)
                title.save()
            except Exception as e:
                raise CommandError(e)


class Command(BaseCommand):
    help = 'Load csv files into the database'

    def handle(self, *args, **options):
        for csv_file, model in CSV_FILES:
            process_file(csv_file, model)
        process_genre_title()
