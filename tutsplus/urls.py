from django.conf.urls import patterns, include, url
from django.views.generic import DetailView, ListView
from tutsplus.models import Tutsplus


urlpatterns = patterns('', 
	url(r"^$", 
		ListView.as_view(
			queryset = Tutsplus.objects.order_by('-id')[:5],
			context_object_name = 'tuts_list',
			template_name = 'index.html'
		)
	),
	
	# url(r"^(?P<pk>\d+)/$",
	# 	DetailView.as_view(
	# 		model=Poll,
	# 		template_name='detail.html'
	# 	)
	# ),
	
	# url(r"^(?P<pk>\d+)/results/$",
	# 	DetailView.as_view(
	# 		model = Poll,
	# 		template_name = 'results.html'
	# 	),
	# 	name = 'poll_results'
	# ),
	
	# url(r"^(?P<poll_id>\d+)/vote/$", 'polls.views.vote'),
	
	
)
