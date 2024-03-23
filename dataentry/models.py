from django.db import models

class Student(models.Model):
    roll_num = models.CharField(max_length=9)
    name = models.CharField(max_length=25)
    age=  models.IntegerField()

    def __str__(self):
        return self.name 


class Employee(models.Model):
    name = models.CharField(max_length=250)
    industry = models.CharField(max_length=255)
    company = models.CharField(max_length=100)
    mobile = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    website = models.CharField(max_length=100)
    

    def __str__(self):
        return f"{self.name} - {self.company}"
    

class Customer(models.Model):
    name = models.CharField(max_length=250)
    country = models.CharField(max_length=255)


    def __str__(self):
        return self.name 