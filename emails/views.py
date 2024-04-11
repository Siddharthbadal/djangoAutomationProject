from django.shortcuts import render, redirect
from .forms import EmailForm
from django.contrib import messages
from dataentry.utils import send_email_notification
from .models import Subscriber
from .tasks import send_bulk_email_task

def send_email(request):
    if request.method =='POST':
        email_form = EmailForm(request.POST, request.FILES) 
        if email_form.is_valid():
             email_form= email_form.save()
             
             # send and email 
             mail_subject = request.POST.get('subject')
             print(mail_subject)
             message = request.POST.get('body')
             print(message)
             # get the email list id and name
             email_list = request.POST.get('email_list')
             print(email_list)
             email_list = email_form.email_list
             print(email_list)

             # extract emails from the list 
             subscribers = Subscriber.objects.filter(email_list=email_list)

          #    to_email= []
             to_email =[email.email_address for email in subscribers]
          #    for email in subscribers:
          #         to_email.append(email.email_address)               
             print('to email => ', to_email)

          # check for attachment
             if email_form.attachment:
                  attachment = email_form.attachment.path
             else:
                  attachment = None 
             
          #    from tasks.py
             send_bulk_email_task.delay(mail_subject, message, to_email, attachment)

             # display a success message 
             messages.success(request, 'Email Sent Successfully!')
             return redirect('send_email')

    else:
            email_form = EmailForm()
            context = {
                 'email_form': email_form
            }
            return render(request, 'emails/send_email.html', context)




