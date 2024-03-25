from django.core.management.base import BaseCommand, CommandError
from django.apps import apps 
# from dataentry.models import Employee
import csv
from django.db import DataError


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
        model = None 
        # search for the model accros all apps
        for app_config in apps.get_app_configs():
            # search model in app
            try:
                model = apps.get_model(app_config.label, model_name)
                break # model found 
            except LookupError:
                continue # model not found. search in the next app
        
        if not model:
            raise CommandError(f"{model_name} not found!")
        

        # compare csv file header with the model names for errors
        # get the model fileds name
        model_fields = [field.name for field in model._meta.fields if field.name != 'id']
        # model fields also has ID. needs to exclude 
        print(model_fields)

        with open(file_path, 'r') as file:
            reader = csv.DictReader(file)   
            csv_header = reader.fieldnames
            if csv_header != model_fields:
                      raise DataError(f"CSV headers must match with {model_name} table fields!")
            
            for row in reader:
                    # print(row)
                model.objects.create(**row)
                    # Employee.objects.create(name=row['name'], industry=row['industry'], company=row['company'],mobile=row['mobile'],email=row['email'],website=row['website'])
        self.stdout.write(self.style.SUCCESS(f"CSV File For {model_name} Table Imported Successfully!"))

                

