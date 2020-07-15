from django.shortcuts import render
from django.core.mail import send_mail
from django.http import HttpResponseRedirect, HttpResponse
# Create your views here.
from random import randrange
from .models import User
def login(request):
	return render(request, 'login.html')

def wake(request, otp):
	otp_by_user = request.POST['otp']
	if otp == int(otp_by_user):
		return render(request, 'firstlog.html')
	else:
		return HttpResponse(f"Sorry Wrong Password")
	return render(request, '')
def check(request):
	mail = request.POST['email']
	name = request.POST['nm']
	otp  = randrange(1000, 9999)
	send_mail('otp for spyler mart',
			 f'Hey, {name} your otp is {otp}, enjoy!',
			 'abhilashtalankar@gmail.com',
			 [mail],
			 fail_silently=False
	)
	return render(request, 'give.html', {'OTP': otp, 'name': name})


def join(request):
	name = request.POST['nm']
	Password = request.POST['pass']
	new_user = User(name=name, password=Password)
	new_user.save()
	return HttpResponseRedirect('/')