from django.db import models

# Create your models here.
from fb.models import *

from django.contrib import admin
from django.forms import ModelForm
from django.utils.translation import ugettext_lazy as _

from django.template.defaultfilters import slugify

class FBUserProfileForm(ModelForm):
	
	def __init__(self, *args, **kwargs):
		#initial = kwargs.get('initial', {} )
		#initial['fb_id'] = args[0].get('id')
		#kwargs['initial'] = initial
		
		super(FBUserProfileForm, self).__init__(*args, **kwargs)
		
		# Dont know y kwargs is not working & args is working
		#self.instance.fb_id = kwargs.get('id')
		# Dont know y kwargs is not working & args is working
		#self.instance.fb_id = args[0].get('id')
		
	class Meta:
		model = FBUserProfile
		
