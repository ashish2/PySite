from django.conf.urls import patterns, include, url



# Caching
from django.views.decorators.cache import cache_page

from django.contrib.staticfiles.urls import staticfiles_urlpatterns
#from django.conf import settings
#from django.conf import settings

from mysite.settings import STATIC_URL


urlpatterns = patterns('search.views', 
	
	# Default
	url(r"", "search" ), # search
	# url(r"", "main" ), # search
	
)


