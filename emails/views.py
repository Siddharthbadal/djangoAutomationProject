from django.shortcuts import render, redirect
from .forms import EmailForm
from django.contrib import messages

def send_email(request):
    if request.method =='POST':
        email_form = EmailForm(request.POST, request.FILES) 
        if email_form.is_valid():
             email_form.save()
             # send and email 


             #display a success message 
             messages.success(request, 'Email Sent Successfully!')
             return redirect('send_email')

    else:
            email_form = EmailForm()
            context = {
                 'email_form': email_form
            }
            return render(request, 'emails/send_email.html', context)




