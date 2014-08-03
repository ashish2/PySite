from django.conf.urls import patterns, include, url
from django.views.generic import DetailView, ListView


# Importing views
from minbase.includes import *
from async.views import *


urlpatterns = patterns('async.views', 
	
	
	# Default
	url(r"", "main" ),
	
)





