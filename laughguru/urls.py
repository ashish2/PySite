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
#from q_a.api import *

#v1_api = Api(api_name='v1')
#v1_api.register(UserResource())
#v1_api.register(PostResource())
# Api-


urlpatterns = patterns('laughguru.views', 
	
	# Add reply, & comments ( later when we have comments table linked )
	#url(r"^stpros/add/reply/(\d+)/?", "add_reply"),
	
	# url(r"^create/", "create"), 		# Add post, Add question, add/ , add_new
	url(r"^questions/r/(\d+)/", "read"), 		# Show Details, of Stpros id
	url(r"^questions/r/result/", "result"), 		# Show Details, of Stpros id
	# url(r"^read/(\d+)/", "read_pts_n_answers"), 		# Show Details, of Stpros id
	# url(r"^pts/d/(\d+)/", "ptsD"),
	
	# url(r"^reply/(\d+)/$", "add_reply"),

	# url(r"^vote/(?P<pk>\d+)/(?P<vote>-?\d+)/", "vote"),
	
	# url(r"^fave/c/(?P<pk>\d+)/", "faveC"), # faveC: Fave Create
	# url(r"^fave/d/(?P<pk>\d+)/", "faveD"), # faveD: Fave Delete
	
	
	#url(r"^api/", include(v1_api.urls ) ), 		# Stpros Api 	# Api-
	
	# Default
	# url(r"/?", "list_all" ), # list all stpros
	
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



