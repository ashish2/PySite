from django.db import models

# Create your models here.
from q_a.models import *
from laughguru.models import *

from django.contrib import admin
from django.forms import ModelForm
from django.utils.translation import ugettext_lazy as _

from django.template.defaultfilters import slugify

#from minbase.includes import *
from django.forms import TextInput


#from django import forms 

class QuestionsForm(ModelForm):
	class Meta:
		model = Questions
		exclude = ( 'is_active',  )
		# widgets = {
		# 	'problem': TextInput(attrs={'size': 40, 'class': "form-control"}  )
		# }
		
		# labels?
		# labels = {
		# 	'problem': "Problem Statement",
		# }
		
	# def __init__(self, *args, **kwargs):
	# 	exclude_list = None
	# 	# If exclude is there, remove some fields from the Form
	# 	if kwargs.get('exclude'):
	# 		exclude_list = kwargs.pop('exclude')
	# 	super(PathToSolutionForm, self).__init__(*args, **kwargs)
		
	# 	# Removing Form Fields
	# 	if exclude_list:
	# 		for field in exclude_list:
	# 			del self.fields[field]
		
	# 	if self.fields.get('problem'):
	# 		self.fields['problem'].label = "A problem that you were up against"
	# 		self.fields['answer'].label = "How you solved it, and steps to the solution"
		
	
	# def save(self, request, commit=True):
	# 		instance = super(PathToSolutionForm, self).save(commit=False)
	# 		instance.user = request.user
	# 		if commit:
	# 			instance.save()
	# 		return instance
		


