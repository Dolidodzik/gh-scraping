from django.core.management.base import BaseCommand, CommandError

class Command(BaseCommand):
    help = "Scrapes github users from provided link into database"

    def add_arguments(self, parser):
        parser.add_argument('--repo_name')

    def handle(self, *args, **options):
        print("hello world")
        print(options['repo_name'])