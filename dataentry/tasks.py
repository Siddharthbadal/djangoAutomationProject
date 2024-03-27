from auto_main.celery import app
import time 
from django.core.management import call_command

@app.task
def celery_test_task():
    print("1 second")
    time.sleep(10)
    print("10 seconds")
  
    return "Task executed successfully from tasks.py!"

@app.task 
def import_data_task(file_path, model_name):
    """
        Function calls the custome commands import data. 
        Takes two arguments file_path, model_name
    """
    try:
        # call_commands calls the custom comnads in views 
        call_command("importdata", file_path, model_name)        
    except Exception as e:
        raise e
    return "Data imported successfully!"