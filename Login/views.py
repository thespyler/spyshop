from django.shortcuts import render
from django.core.mail import send_mail
from django.http import HttpResponseRedirect, HttpResponse
from random import randrange # to generate otp
from .models import User



def login(request):
	# Renders the Main login Page
	return render(request, 'login.html')


def wake(request, otp):
	# Check if the otp entered by the user is valid or not if yes then 
	# Make him to enter his name and password to signin, else tell him
	# to try again

	otp_by_user = request.POST['otp']
	if otp == int(otp_by_user):
		return render(request, 'firstlog.html')
	else:
		return HttpResponse(f"Sorry Wrong Password")



def check(request):
	# Send the email to the user and generate an otp, after the email
	# is sent successfuly render the template to enter the correct otp

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
	# Create a table in the database and save him using the django models
	# return to the login page after that

	name = request.POST['nm']
	Password = request.POST['pass']
	new_user = User(name=name, password=Password)
	new_user.save()
	return HttpResponseRedirect('/')



def start_page_log(request):
	# if the user wants to login, make him enter his name and password
	# look for the person in the database and check if he has entered the
	# correct Password, if yes redirect him to the shop page, else tell him
	# that his password is incorrect

	name = request.POST['nm']
	password = request.POST['pass']
	
	for i in User.objects.all():
		if i.name == name:
			if i.password == password:
				return HttpResponseRedirect('/shop/')

		else:
			return HttpResponse("Wrong Username or Password")