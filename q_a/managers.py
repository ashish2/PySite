from django.db import models

# Create your models here.
from q_a.models import *

from django.contrib import admin

from django.forms import ModelForm
from django.utils.translation import ugettext_lazy as _


### Managers

class PostManager(models.Manager):
	
	def title_count(self, keyword):
		return self.filter(title__icontains=keyword).count()
	
	
	def _get_full_name(self):
		""" returns self ttile"""
		return super(PostManager, self).get_query_set().filter(title='t')
	
	


