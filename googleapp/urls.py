from django.conf.urls import patterns, include, url
from django.views.generic import DetailView, ListView


# Importing views
from q_a.views import *

from googleapp.models import *

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


urlpatterns = patterns('googleapp.views', 
	

	url(r"^attendance/create/", "create", name="attendance_create"), 		# Add post, Add question, add/ , add_new
	url(r"^attendance/(?P<pk>\d+)/edit/", "edit"), 		# Show Details, of Stpros id

	# url(r"^read/(?P<pk>\d+)/", "read"), 		# Show Details, of Stpros id

	# url(r"^login/", "login"), 		# login

	url(r"^list_all/$", "list_all", name="googleapp_attendance_list_all"
	),

	#url(r"^api/", include(v1_api.urls ) ), 		# Stpros Api 	# Api-
	# Default
	url(r"/", 
		ListView.as_view(
			# queryset = Guser.objects.filter(request.user.guser_id).order_by('-pub_date'),
			queryset = Attendance.objects.order_by('-pub_date'),
			context_object_name = 'somelist',
			template_name = 'ga_some_list.html'
		),
 ), # list all from
	
	#~url(r"^(?P<pk>\d+)/$",
		#~DetailView.as_view(
			#~model=Poll,
			#~template_name='detail.html'
		#~)
	#~),

	
)





