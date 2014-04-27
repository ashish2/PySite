from django.conf.urls import patterns, include, url
from django.views.generic import DetailView, ListView


# Importing views
from q_a.views import *

# Caching
from django.views.decorators.cache import cache_page

from django.contrib.staticfiles.urls import staticfiles_urlpatterns
#from django.conf import settings
#from django.conf import settings

from mysite.settings import STATIC_URL

# Api
from django.conf.urls.defaults import *
from tastypie.api import *
from q_a.api import *

v1_api = Api(api_name='v1')
v1_api.register(UserResource())
v1_api.register(PostResource())
# Api-


urlpatterns = patterns('q_a.views', 
	
	# Post form to add Question
	url(r"^post/form/$", "show_post_form"),
	
	# Post form to add Reply to Answers
	url(r"^post/reply/(\d+)/?$", "show_reply_form"),
	
	# Add Reply to Asnwers
	url(r"^post/add/reply/(\d+)/?", "add_reply"),
	# Add post, Add question
	url(r"^post/add/?", "add_post"),
	
	# Add an Answer
	#~url(r"^post/answer/?", "add_answer"),
	
	# Share
	url(r"^post/share/(?P<pk>\d+)/(?P<share>-?\d+)", "share"),
	
	
	# RANDOM
	url(r"^post/random", "random"),
	
	# RANDOM/-
	
	# Static
	#url(r'^static/(?P<path>.*)$', 'staticfiles.views.serve'),
	
	# Static/-
	
	# Vote +1 or -1
	#url(r"^post/votem/(?P<pk>\d+)/(?P<vote>\d+)/", "votem"),
	
	url(r"^post/vote/(?P<pk>\d+)/(?P<vote>-?\d+)/?", "vote"),
	url(r"^post/follow/(?P<pk>\d+)/(?P<follow>-?\d+)/(?P<typ>\w?)/?", "follow"),
	
	
	url(r"^post/(?P<pk>\d+)/(?P<slug>[a-z0-9-]+)", "view_post_id"),
	
	# Generic url mappings should go down in the last
	url(r"^post/?", "view_all_post" ),
	# Cacheing the same above page with this below
	# url(r"^post/?", cache_page( view_all_post, 60*10) ), # Here, adding cache to the above function.
	
	# q_a Api
	url(r"^api/", include(v1_api.urls ) ),
	# Api-
	
	# Default
	url(r"", "view_all_post" ),
	
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




