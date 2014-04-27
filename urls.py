from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from django.conf import settings

import os
cwd = os.getcwd()

from emailusernames.forms import EmailAuthenticationForm

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
	
	
	### Testapps//
	
	# Tiny mce
	(r'^tiny_mce/(?P<path>.*)$', 'django.views.static.serve', {'document_root': cwd +'/static/tinymce/js/tinymce'} ),
	
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
	url(r"^accounts/login/$", "django.contrib.auth.views.login", {'authentication_form': EmailAuthenticationForm}, name = "login" ),
	url(r"^accounts/logout/$", "django.contrib.auth.views.logout", {'template_name': 'registration/logout.html'}, name = "logout" ),
	
	# Login/Logout-
	
	
	# Uncomment the next line to enable the admin:
	url(r'^admin/', include(admin.site.urls)),
	
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
