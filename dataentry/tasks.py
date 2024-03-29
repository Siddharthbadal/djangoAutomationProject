from auto_main.celery import app
import time 
from django.core.management import call_command
from django.core.mail import EmailMessage
from django.conf import settings
from .utils import send_email_notification


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
    
    # send an email
    mail_subject="Data Import Notification"
    message=f"""
            Your data for table {model_name} is imported now. You can check the data table at admin panel.
            Thank you. 
    """    
    to_email= settings.DEFAULT_TO_EMAIL
    send_email_notification(mail_subject, message, to_email)
    return "Data imported successfully. Email Alert Sent!"