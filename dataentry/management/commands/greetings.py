# demo command 
from django.core.management.base import BaseCommand

# proposed command = python manage.py greetings 'name-argument'
class Command(BaseCommand):
    help= "Greets the User"  # command --help text

    def add_arguments(self, parser):
        parser.add_argument('name', type=str, help='Spcifies user name') # argument --help text

    def handle(self, *args, **kwargs):
        name=kwargs['name']
        greeting = f"Good Morning, {name}!"
        # self.stdout.write(greeting)
        self.stdout.write(self.style.SUCCESS(greeting))
        self.stdout.write(self.style.WARNING(greeting))

    