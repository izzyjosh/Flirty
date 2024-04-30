# myapp/management/commands/load_data.py

import json
from django.core.management.base import BaseCommand
from main.models import Category, Quote

class Command(BaseCommand):
    help = 'Load data from JSON file into the database'

    def add_arguments(self, parser):
        parser.add_argument('file_path', type=str, help='Path to the JSON file')

    def handle(self, *args, **options):
        file_path = options['file_path']
        
        with open(file_path, 'r') as f:
            data = json.load(f)

            for category_data in data['Category']:
                category = Category.objects.create(**category_data)

            for quote_data in data['Quote']:
                category_id = quote_data.pop('category')
                category = Category.objects.get(id=category_id)
                Quote.objects.create(category=category, **quote_data)

        self.stdout.write(self.style.SUCCESS('Data loaded successfully'))
