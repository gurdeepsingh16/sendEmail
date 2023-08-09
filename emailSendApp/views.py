from django.shortcuts import render,HttpResponse
from django.conf import   settings
from django.core.mail import   send_mail
# Create your views here.

def home(re):
    subject = 'welcome to Our website'
    message = f'Hi "gurdeep, thank you for registering in our website.'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = ["singhgurdeep6360@gmail.com"]
    send_mail( subject, message, email_from, recipient_list )
    return HttpResponse("hello") 