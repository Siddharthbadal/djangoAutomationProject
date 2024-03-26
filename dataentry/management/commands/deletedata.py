from django.core.management.base import BaseCommand, CommandError
from django.apps import apps 
from dataentry.models import CompanyData
import csv

# proposed command python manage.py deletedata csv_file_path
# proposed command python manage.py deletedata csv_file_path modal_name

class Command(BaseCommand):
    help = "Delete Data From a CSV File"

    def add_arguments(self, parser):
        parser.add_argument('model_name',type=str,help='model name')
        

        

    def handle(self, *args, **kwargs):
        # command logic
                
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
        
        # print(row)
        data = model.objects.all()
        data.delete()
        # Employee.objects.create(name=row['name'], industry=row['industry'], company=row['company'],mobile=row['mobile'],email=row['email'],website=row['website'])
        self.stdout.write(self.style.SUCCESS(f"Deleted all the data from {model_name} table successfully!"))

               

