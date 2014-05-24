from django.db import models

# Create your models here.
from q_a.models import *

from django.contrib import admin
from django.forms import ModelForm
from django.utils.translation import ugettext_lazy as _

from django.template.defaultfilters import slugify

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

#======

def myPostForm(**kwargs):
	if kwargs.has_key("exclude_list"):
		e = kwargs["exclude_list"]
	else:
		e = []
	
	ex = ['slug', 'parent_id', 'date', 'user', 'user_ip', 'status', 'tags']
	ex.extend(e)
	
	class PostForm(ModelForm):
		
		def __init__(self, *args, **kwargs):
			super(PostForm, self).__init__(*args, **kwargs)
			if self.fields.get('title'):
				#self.fields['title'].label = "List Experience or an Event that you went through or Ask Question about an Experience that yuo think you will go through and you need an answer to it before hand"
				self.fields['title'].label = "List Life Experience or Life Event that you would like to share"
		
		#def save(self, request, *args, **kwargs):
			#post =super(PostForm, self).save(commit=False)
			#if not self.id:
			#post.slug = slugify(self.title)
			# create tags too, if tag field is field, then, loop on their commas & create tag field. for each comma, we'll hv to clie
			#post.tags = self.cleaned_data["tags"]
			#post.save()
			#return post
		
		class Meta:
			model = Post
			exclude = ex
			
	
	return PostForm()
	

# Instead of myPostForm function, having just PostForm class
# see how you can consolidate
class PostForm(ModelForm):
	
	def __init__(self, *args, **kwargs):
		super(PostForm, self).__init__(*args, **kwargs)
		if self.fields.get('title'):
			#self.fields['title'].label = "List Experience or an Event that you went through or Ask Question about an Experience that yuo think you will go through and you need an answer to it before hand"
			self.fields['title'].label = "List Life Experience or Life Event that you would like to share"
	
	class Meta:
		model = Post
		exclude = ['slug', 'parent_id', 'date', 'user', 'user_ip', 'status', 'tags']
		

#======

class ImagesForm(ModelForm):
	class Meta:
		model = Images
		exclude=('post',)
