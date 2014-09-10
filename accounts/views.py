# Create your views here.

from minbase.includes import *

#~def login(request, template_name):
	#~
	#~login(request)
	#~
	#~return HttpResponse(template_name)
	#~return HttpResponse("Hi")

#~def logout_view(request):
	#~logout(request)
	#~return render_to_response('registration/logout.html')
	

from django import forms
#from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.shortcuts import render

from emailusernames.utils import create_user, create_superuser, get_user
from emailusernames.forms import user_exists

from accounts.forms import RegistrationForm


def register(request):
	#create_superuser('admin@example.com', 'password')
	
	form = RegistrationForm()
	if request.method == 'POST':
		form = RegistrationForm(request.POST)
		
		if form.is_valid():
			# Check this, change it to email in html template
			# in html, the input element has name as 'username', but we are showing label as email, so we will accept it as 'email'
			email = request.POST.get('username')
			password = request.POST.get('password1')
			
			# There are errors, if the email gets repeated,
			# check, some authentication, if UserValid only then fire a create_user, else, print some error in html
			
			if not user_exists(email):
				create_user(email, password)
			else: # if user exists, then log him in
				# If user created properly, then login
				# This login is NOT WORKING, see y?
				#import django.contrib.auth.views as v
				#v.login(request)
				pass
			
			return HttpResponseRedirect("/")
			
		else:
			form = RegistrationForm(request.POST)
	
	#return render(request, "registration/register.html", { 'form': form, })
	return render(request, 'registration/registration.html', { 'form': form, }, context_instance=RequestContext(request))
	
