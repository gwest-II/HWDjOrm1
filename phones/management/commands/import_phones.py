import csv
from django.template.defaultfilters import slugify
from django.core.management.base import BaseCommand
from phones.models import Phone


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('phones.csv', 'r') as file:
            phones = list(csv.DictReader(file, delimiter=';'))

            for phone in phones:
                phone_db = Phone(id=phone.get('id'), name=phone.get('name'), price=phone.get('price'),
                                 image=phone.get('image'), release_date=phone.get('release_date'),
                                 lte_exist=bool(phone.get('lte_exist')), slug=slugify(phone.get('name')))
                phone_db.save()

        # TODO: Добавьте сохранение модели phone in phones:
