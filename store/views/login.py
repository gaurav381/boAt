from django.shortcuts import render , redirect , HttpResponseRedirect

from django.contrib.auth.hashers import  check_password
from store.models.customer import Customer
from django.views import  View
from django.core.mail import send_mail
from Eshop import settings
import requests
import json
import random


class Login(View):
    return_url = None
    def get(self , request):
        Login.return_url = request.GET.get('return_url')
        return render(request , 'login.html')
    
    def post(self , request):
        email = request.POST.get('email')
        password = request.POST.get('password')
        customer = Customer.get_customer_by_email(email)
        error_message = None
        if customer:
            flag = check_password(password, customer.password)
            if flag:

                    #Send Mail
    
                subject='Re:signup Successfully'
                msg="Hello [Admin],\nThank you. We are delighted to have you with us.\nWe hope you find in our business what you are looking for.\nSomeone from our customer care team will get in touch within 24 hours.\nstudent_management Pvt Ltd \n +91 9876512597 |student@int.com \n\n Respectfully,\n@student_management"
                #msg="Hello User, \nYour account has been created successfully! \nEnjoy our services. \n Thanks & Regards, \nBatchProject - TOPS Technologoies Pvt Ltd \n +91 9998506434 | sanketchauhanios@gmail.com"
                from_email=settings.EMAIL_HOST_USER
                #to_email=['gk.vekariya000@gmail.com']
                to_email=[request.POST['email']]
                send_mail(subject,msg,from_email,to_email)
                   #return redirect('admin_home')
                request.session['customer'] = customer.id

                if Login.return_url:
                   return HttpResponseRedirect(Login.return_url)
                else:
                    Login.return_url = None
                    return redirect('homepage')
            else:
                error_message = 'Email or Password invalid !!'
        else:
            error_message = 'Email or Password invalid !!'

        print(email, password)
        return render(request, 'login.html', {'error': error_message})

def logout(request):
    request.session.clear()
    return redirect('login')
