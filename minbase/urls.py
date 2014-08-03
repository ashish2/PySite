from django.conf.urls import patterns, include, url
from django.views.generic import DetailView, ListView


# Importing views
from minbase.views import *


urlpatterns = patterns('minbase.views', 
	
	
	# Post form to add Reply to Answers
	url(r"^fb_login/$", "fb_login"),
	

	# Default
	#url(r"", "view_all_post" ),
	
)





