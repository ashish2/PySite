from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from django.conf import settings

import os
cwd = os.getcwd()

from emailusernames.forms import EmailAuthenticationForm

# for Haystack
from django.core import management
import mysite.settings as settings
management.setup_environ(settings)
#-

# RESTAPI

### Rest_framework

from django.contrib.auth.models import User, Group
#~from rest_framework import viewsets, routers

# ViewSets define the view behavior.
#~class UserViewSet(viewsets.ModelViewSet):
	#~model = User
#~
#~class GroupViewSet(viewsets.ModelViewSet):
	#~model = Group


# Routers provide an easy way of automatically determining the URL conf
#~router = routers.DefaultRouter()
#~router.register(r'users', UserViewSet)
#~router.register(r'groups', GroupViewSet)


### Tastypie



# RESTAPI-


urlpatterns = patterns('',
	# Examples:
	# url(r'^$', 'mysite.views.home', name='home'),
	# url(r'^mysite/', include('mysite.foo.urls')),

	# Uncomment the admin/doc line below to enable admin documentation:
	url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
	
	
	# Polls
	url(r"^polls/", include("polls.urls")),
	
	# QnA
	url(r"^qna/", include("qna.urls")),
	
	### Testapps 
	
	# Q_A
	url(r"^q_a/", include("q_a.urls")),
	
	
	# Users
	url(r"^users/", include("users.urls")),
	
	# Followers_following
	url(r"^follow/", include("following_followers.urls")),
	
	# Stpros
	url(r"^stpros/", include("stpros.urls")),
	
	# FB
	url(r"^hi_from_fb", "stpros.views.hi_from_fb"),
	
	#Minbase
	url(r"^minbase/", include("minbase.urls")),
	
	# async
	url(r"^async/", include("async.urls")),
	
	
	### Testapps//
	
	# Tiny mce
	(r'^tiny_mce/(?P<path>.*)$', 'django.views.static.serve', {'document_root': cwd +'/static/tinymce/js/tinymce'} ),
	
	# wysibb
	(r'^wysibb/(?P<path>.*)$', 'django.views.static.serve', {'document_root': cwd +'/static/wysibb'} ),
	
	
	# Static
	(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': cwd +'/static/'} ),
	# Static/
	
	# Login/Logout
	#~(r'^accounts/login/$',  login),
	#~(r'^accounts/logout/$', logout),
	
	# Accounts -> Users
	#~url(r"^accounts/", include("accounts.urls") ),
	
	
	# Login/Logout form
	
	#~url(r"^auth/$", include("accounts.urls") ),
	#~url(r"^auth/logout/?$", "accounts.views.logout_view" ),
	# Login
	url(r"login/$", "django.contrib.auth.views.login", {'authentication_form': EmailAuthenticationForm}, name = "login" ),
	# Logout
	url(r"logout/$", "django.contrib.auth.views.logout", {'template_name': 'registration/logout.html'}, name = "logout" ),
	
	url(r"^accounts/", include("accounts.urls") ),
	
	# Login/Logout-
	
	# RESTAPI
	#url("^api/auth/", include('rest_framework.urls', namespace='rest_framework')),
	#~url(r'^api/', include(router.urls)),
	
	#url("^api/", "q_a.views.view_all_post" ),
	
	
	# RESTAPI-
	
	# Haystack Search
	#(r'^haystack_search/', include('haystack.urls')),
	# Haystack Search-
	
	# Uncomment the next line to enable the admin:
	url(r'^admin/', include(admin.site.urls)),
	
	# Default
	url(r"", include("q_a.urls") ), 
	
)


# Static Files
"""
if settings.DEBUG:
	urlpatterns += (
		
		url(r'^static/(.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
		
		url(r'^media/(.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
		
	)
	
"""
	
#urlpatterns += staticfiles_urlpatterns()
