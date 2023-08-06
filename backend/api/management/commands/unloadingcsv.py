import csv

from django.core.management.base import BaseCommand
from foodgram.settings import CSV_FILES_UP
from recipe.models import Ingredient


class Command(BaseCommand):

    def handle(self, *args, **options):
        with open(
                f'{CSV_FILES_UP}/ingredients.csv',
                encoding='utf-8'
        ) as file:
            reader = csv.reader(file)
            for item in reader:
                name, unit = item
                Ingredient.objects.get_or_create(
                    name=name,
                    measurement_unit=unit
                )

        print('Добавлены ингредиенты', Ingredient.objects.count())
