from django.core.management.base import BaseCommand
from dataentry.models import Employee
import csv

# proposed command python manage.py importdata csv_file_path
# proposed command python manage.py importdata csv_file_path modal_name

class Command(BaseCommand):
    help = "Import Data From a CSV File"

    def add_arguments(self, parser):
        parser.add_argument('file_path',type=str,help='csv file path')
        

        

    def handle(self, *args, **kwargs):
        # command logic
        file_path = kwargs['file_path']
        # print(file_path)
        


        with open(file_path, 'r') as file:
            reader = csv.DictReader(file)
            
            for row in reader:
                pre_name = row['name']
                existing_record = Employee.objects.filter(name=pre_name).exists()

                if not existing_record:

                    # print(row)
                    Employee.objects.create(**row)
                    # Employee.objects.create(name=row['name'], industry=row['industry'], company=row['company'],mobile=row['mobile'],email=row['email'],website=row['website'])
                    self.stdout.write(self.style.SUCCESS("CSV File Imported successfully!"))

                else:
                    self.stdout.write(self.style.WARNING(f"data for {pre_name} already exist!"))


