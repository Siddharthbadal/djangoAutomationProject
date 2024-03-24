import csv 
import datetime 
from django.core.management import BaseCommand, CommandError
from django.apps import apps
from django.core.management.base import CommandParser 
from dataentry.models import Employee

# proposed commaand - python manage.py exportdata


class Command(BaseCommand):
    help =" Export data to CSV file from any database"

    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument('model_name', type=str, help='Model name') 

    def handle(self, *args, **kwargs):
        model_name = kwargs['model_name']
        model = None 

        for app_config in apps.get_app_configs():
            try:
                model = apps.get_model(app_config.label, model_name)
                break 
            except LookupError:
                continue 

        if not model:
            raise CommandError(f"Table {model_name} not found!")
            return 

        # fetch data from database  
        model_data = model.objects.all()
        # print(model_data)

        # current date time
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S") 
        # csv file details
        file_path = f"E:\django\Exported_{model_name}_data_{timestamp}.csv"
        print(file_path)


        # open and write the file 
        with open(file_path, "w", newline="") as file:
            writer = csv.writer(file)
            # write csv rows 
            # writer.writerow(
            #     ['name', 'industry','company','mobile','email', 'website']
            # )

            # print field names of the given model
            writer.writerow(
                [field.name for field in model._meta.fields]
            )

            for data in model_data:
                writer.writerow(
                    [getattr(data, field.name) for field in model._meta.fields]
                )
                # writer.writerow(
                #     [data.name,
                #      data.industry,
                #      data.company,
                #      data.mobile,
                #      data.email,
                #      data.website
                #      ]
                # )

        self.stdout.write(self.style.SUCCESS(f'Data Exported Successfully from {model_name} table!'))