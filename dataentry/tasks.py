from auto_main.celery import app
import time 
from django.core.management import call_command
from django.core.mail import EmailMessage
from django.conf import settings
from .utils import send_email_notification, generate_csv_file


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
            Your data for table {model_name} is imported now. 
            You can check the data table at admin panel.
            
            Thank you. 
    """    
    to_email= settings.DEFAULT_TO_EMAIL
    send_email_notification(mail_subject, message, to_email)
    return "Data imported successfully. Email Alert Sent!"


@app.task 
def export_data_task(model_name):
    """
    Export database model into a csv file on your computer. 
    Funtions takes one argument. 
    """
    try:
        call_command('exportdata', model_name)
    except Exception as e:
        raise e
    
    file_path= generate_csv_file(model_name)
    print(file_path)

    # sent an email with attachment csv file. 
    mail_subject="Data Export Notification"
    message=f"""
            Data for table {model_name} exported successfully. 
            Please Find the attached file.

            Thank you. 
    """    
    to_email= settings.DEFAULT_TO_EMAIL
    send_email_notification(mail_subject, message, to_email, attachment=file_path)
    
    return "Data Exported Successfully. Email alert sent!"