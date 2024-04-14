from auto_main.celery import app
from dataentry.utils import send_email_notification

@app.task 
def send_bulk_email_task(mail_subject, message, to_email, attachment):
     """ function to send bulk email. called in views.py with argumnents."""
     send_email_notification(mail_subject, message, to_email, attachment)
     return 'Email sent tasks executed!'