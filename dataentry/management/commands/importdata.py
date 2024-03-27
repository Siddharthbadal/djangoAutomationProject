from django.core.management.base import BaseCommand, CommandError
from django.apps import apps 
# from dataentry.models import Employee
import csv
from dataentry.utils import check_csv_errors


# proposed command - python manage.py importdata csv_file_path modal_name

class Command(BaseCommand):
    help = "Import Data From a CSV File"

    def add_arguments(self, parser):
        parser.add_argument('file_path',type=str,help='csv file path')
        parser.add_argument('model_name',type=str,help='model name')

        

    def handle(self, *args, **kwargs):
        # command logic
        file_path = kwargs['file_path']
        # print(file_path)
        model_name = kwargs['model_name']
        
        model = check_csv_errors(file_path, model_name)
        
        with open(file_path, 'r') as file:
            reader = csv.DictReader(file)        
            for row in reader:
                    # print(row)
                model.objects.create(**row)
                    # Employee.objects.create(name=row['name'], industry=row['industry'], company=row['company'],mobile=row['mobile'],email=row['email'],website=row['website'])
        self.stdout.write(self.style.SUCCESS(f"CSV File For {model_name} Table Imported Successfully!"))

                

