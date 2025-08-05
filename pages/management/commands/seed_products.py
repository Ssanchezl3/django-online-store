from django.core.management.base import BaseCommand
from pages.factories import ProductFactory

class Command(BaseCommand):
    help = 'Seed the database with sample products'

    def handle(self, *args, **kwargs):
        for _ in range(10):  # Change 10 to however many products you want to create
            ProductFactory.create()
        self.stdout.write(self.style.SUCCESS('Successfully seeded products'))
