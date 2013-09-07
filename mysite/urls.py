from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

import os
cwd = os.getcwd()

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
    
    (r'^tiny_mce/(?P<path>.*)$', 'django.views.static.serve', {'document_root': cwd +'/static/tinymce/js/tinymce'} ),
    
    
    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    
)
