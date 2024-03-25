from django.contrib import admin
from .models import Student, Employee, Customer, CompanyData


admin.site.register(Student)
admin.site.register(Employee)
admin.site.register(Customer)
admin.site.register(CompanyData)