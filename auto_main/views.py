from django.shortcuts import render
from django.http import HttpResponse
from dataentry.tasks import celery_test_task



def home(request):
   return render(request, 'index.html')


# celery test 

def celery_test(request):
   print("Processing.. .")
   celery_test_task.delay()
   print("Proccessed..!")
   
   return HttpResponse("Function executed successfully from auto_main views py!")