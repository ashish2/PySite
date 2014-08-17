from django.conf.urls import patterns, include, url
from django.views.generic import DetailView, ListView

# Importing views
from q_a.views import *

# Caching
from django.views.decorators.cache import cache_page

from django.contrib.staticfiles.urls import staticfiles_urlpatterns
#from django.conf import settings
from django.conf import settings

from users.forms import *

urlpatterns = patterns('users.views',
	
	#~url(r"^$", "index"),
	#~url(r"^(?P<poll_id>\d+)/$", "detail"),
	#~url(r"^(?P<poll_id>\d+)/results/$", "results"),
	
	url(r"^profile/edit/(?P<pk>\d+)/?$", "edit_user_profile", name="edit_user_profile"),
	url(r"^(?P<pk>\d+)/?$", "view_user_profile", name="view_user_profile"),

	
	#url(r"edit/$", "user_edit_form" ),
	#url(r"edit$", "user_edit_form" ),
	
	
	#~url(r"^profile/(?P<pk>\d+)/?", "view_userProfile"),
	
	
	#~url(r"", "view_user_profile"),
	
	#~
	#~url(r"^$", 
		#~ListView.as_view(
			#~queryset = Poll.objects.order_by('-pub_date')[:5],
			#~context_object_name = 'latest_poll_list',
			#~template_name = 'index.html'
		#~)
	#~),
	
	#~url(r"^(?P<pk>\d+)/$",
		#~DetailView.as_view(
			#~model=Poll,
			#~template_name='detail.html'
		#~)
	#~),
	
	#~url(r"^(?P<pk>\d+)/results/$",
		#~DetailView.as_view(
			#~model = Poll,
			#~template_name = 'results.html'
		#~),
		#~name = 'poll_results'
	#~),
	#~
	#~url(r"^(?P<poll_id>\d+)/vote/$", 'polls.views.vote'),
	#~
)




