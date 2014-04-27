from django.db import models

# Create your models here.
from q_a.models import *

from django.contrib import admin
from django.forms import ModelForm
from django.utils.translation import ugettext_lazy as _


### Forms
#~def myPostForm(exclude_list):
	#~class PostForm(ModelForm):
		#~
		#~def __init__(self, *args, **kwargs):
			#~if kwargs.has_key("exclude_list"):
				#~exclude = kwargs["exclude_list"]
				#~del kwargs["exclude_list"]
				#~
				#~super(PostForm, self).__init__(self, *args, **kwargs)
				#~for f in exclude:
					#~del self.fields[f]
					#~
			#~else:
				#~exclude = []
			#~
		#~class Meta:
			#~model = Post
	#~
	#~return PostForm()
	#~


def myPostForm(**kwargs):
	if kwargs.has_key("exclude_list"):
		e = kwargs["exclude_list"]
	else:
		e = []
	
	ex = ['slug', 'parent_id', 'date', 'user', 'user_ip', 'status']
	ex.extend(e)
	
	class PostForm(ModelForm):
		
		def __init__(self, *args, **kwargs):
			super(PostForm, self).__init__(*args, **kwargs)
			if self.fields.get('title'):
				self.fields['title'].label = "List Experiance/Event or Ask Question"
			
		class Meta:
			model = Post
			exclude = ex
	
	return PostForm()
	


