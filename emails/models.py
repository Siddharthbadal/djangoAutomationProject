from django.db import models
from ckeditor.fields import RichTextField


# email list
class List(models.Model):
    email_list = models.CharField(max_length=50)

    def __str__(self):
        return self.email_list 
    


class Subscriber(models.Model):
    email_list = models.ForeignKey(List, on_delete=models.CASCADE)
    email_address = models.EmailField(max_length=150)

    def __str__(self):
        return self.email_address
    
class Email(models.Model):
    email_list = models.ForeignKey(List, on_delete=models.CASCADE)
    subject = models.CharField(max_length=150)
    body = RichTextField()
    attachment = models.FileField(upload_to="email_attachment", blank=True, null=True)
    sent_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.subject


