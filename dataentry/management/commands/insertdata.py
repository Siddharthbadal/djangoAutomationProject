# adding data to the database 
from dataentry.models import Student
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = "Insert Data into the database"

    def handle(self, *args, **kwargs):
        # adding data 
        dataset = [
            {
                'roll_num':109,
                'name': 'Virat',
                'age':32
            },
            {
                'roll_num':129,
                'name': 'Rahul',
                'age':37
            },
            {
                'roll_num':104,
                'name': 'Jasprit',
                'age':32
            },
            {
                'roll_num':121,
                'name': 'Rajat',
                'age':22
            },
        ]
        # Student.objects.create(roll_num=101, name='Sidd', age=39)
        for data in dataset:
            roll_no = data['roll_num']
            existing_record = Student.objects.filter(roll_num=roll_no).exists()

            if not existing_record:
                Student.objects.create(roll_num=data['roll_num'], name=data['name'],age=data['age'])
                self.stdout.write(self.style.SUCCESS(f'Data for roll number {roll_no} Inserted successfully!'))
            else:
                self.stdout.write(self.style.WARNING(f'Data for roll Number {roll_no} already existed!'))

        

