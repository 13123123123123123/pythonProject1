from django.core.management import BaseCommand


class Command(BaseCommand):

    def handle(self, *args, **options):
        print('23123')