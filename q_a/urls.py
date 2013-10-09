from django.conf.urls import patterns, include, url
from django.views.generic import DetailView, ListView

# Importing views
from q_a.views import *

# Caching
from django.views.decorators.cache import cache_page

from django.contrib.staticfiles.urls import staticfiles_urlpatterns
#from django.conf import settings
from django.conf import settings


urlpatterns = patterns('q_a.views', 
	
	url(r"^post/form/$", "show_post_form"),
	
	url(r"^post/comment/(\d+)/?$", "show_comment_form"),
	
	url(r"^post/add/comment/(\d+)/?", "add_comment"),
	url(r"^post/add/?", "add_post"),
	
	url(r"^post/(?P<pk>\d+)", "view_post_id"),
	
	# Share
	url(r"^post/share/(?P<pk>\d+)", "share"),
	
	
	# RANDOM
	url(r"^post/random", "random"),
	
	# RANDOM/-
	
	
	# Static
	#url(r'^static/(?P<path>.*)$', 'staticfiles.views.serve'),
	
	# Static/-
	
	# Vote +1 or -1
	#url(r"^post/votem/(?P<pk>\d+)/(?P<vote>\d+)/", "votem"),
	
	url(r"^post/vote/(?P<pk>\d+)/(?P<vote>-?\d+)/?", "vote"),
	
	# Generic url mappings should go down in the last
	url(r"^post/?", "view_all_post" ),
	# Cacheing the same above page with this below
	# url(r"^post/?", cache_page( view_all_post, 60*10) ), # Here, adding cache to the above function.
	
	
	
	
	
)


#~urlpatterns = patterns('polls.views',
	#~url(r"^$", "index"),
	#~url(r"^(?P<poll_id>\d+)/$", "detail"),
	#~url(r"^(?P<poll_id>\d+)/results/$", "results"),
	#~url(r"^(?P<poll_id>\d+)/vote/$", "vote"),
	
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
	
#~)




