from django.conf.urls import patterns, include, url
from django.views.generic import DetailView, ListView

# Importing views
from q_a.views import *

# Caching
from django.views.decorators.cache import cache_page

from django.contrib.staticfiles.urls import staticfiles_urlpatterns
#from django.conf import settings
from django.conf import settings

from django.contrib.auth.views import login

from emailusernames.forms import EmailAuthenticationForm

urlpatterns = patterns( 'accounts.views',
	#accounts.views
	
	#
	url(r"register/?$",  "register" ),
	# Login
	#url(r"login/$", "django.contrib.auth.views.login", {'authentication_form': EmailAuthenticationForm}, name = "login" ),
	# Logout
	#url(r"logout/$", "django.contrib.auth.views.logout", {'template_name': 'registration/logout.html'}, name = "logout" ),
	
	# Logout
	#url(r"^logout/?$", "django.contrib.auth.views.logout", { 'template_name': 'registration/logout.html' } ),
	
	# Generic url mappings should go down in the last
	#url(r"", "django.contrib.auth.views.login", { 'template_name': 'registration/login.html' } ),
	
	
)

