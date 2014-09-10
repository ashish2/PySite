# Create your urls here.
from django.conf.urls import patterns, include, url

# Importing views
from q_a.views import *


urlpatterns = patterns('relations.views', 
	
	# Followers of this user id
	url(r"^followers/(?P<pk>\d+)/?$", "show_followers"),
	
	# People whom this user id is following
	url("following/(?P<pk>\d+)/?$", "show_following"),
	
	# add myUid to thatUid, as i will follow him/her
	url("followers/add/(?P<toThatUid>\d+)/(?P<addMyUid>\d+)", "add_followers"),
	
	# i will unfollow him/her, so remove myUid from thatUid
	url("followers/remove/(?P<fromThatUid>\d+)/(?P<removeMyUid>\d+)", "remove_followers"),
	
	url(r"^follow/(?P<wer>\d+)/(?P<wing>\d+)/$", "follow", name="follow"),
	url(r"^unfollow/(?P<wer>\d+)/(?P<wing>\d+)/$", "unfollow", name="unfollow"),
	
)


