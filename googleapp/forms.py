from django.db import models

# Create your models here.
# from q_a.models import *
from googleapp.models import *

from django.contrib import admin
from django.forms import ModelForm
from django.utils.translation import ugettext_lazy as _

from django.template.defaultfilters import slugify

#from minbase.includes import *
# from django.forms import TextInput, DateTimeInput, SplitDateTimeWidget
from django.forms import *


#from django import forms 

class GuserForm(ModelForm):
	class Meta:
		model =  Guser
		exclude = ( 'is_active', 'user',  )
		widgets = {
			'problem': TextInput(attrs={'size': 40, 'class': "form-control"}  )
		}
		
		# labels?
		labels = {
			'problem': "Problem Statement",
		}
		
	def __init__(self, *args, **kwargs):
		exclude_list = None
		# If exclude is there, remove some fields from the Form
		# if kwargs.get('exclude'):
		# 	exclude_list = kwargs.pop('exclude')
		super( GuserForm, self).__init__(*args, **kwargs)
		
		# Removing Form Fields
		# if exclude_list:
		# 	for field in exclude_list:
		# 		del self.fields[field]
		
		# if self.fields.get('problem'):
		# 	self.fields['problem'].label = "A problem that you were up against"
		# 	self.fields['answer'].label = "How you solved it, and steps to the solution"
		
	def save(self, request, commit=True):
		instance = super( GuserForm, self).save(commit=False)
		instance.user_id = request.user.pk
		if commit:
			instance.save()
		return instance
		

class AttendanceForm(ModelForm):
	class Meta:
		model = Attendance

		exclude = ( 'is_active', 'guser', )

		widgets = {
			# 'date': DateTimeInput(attrs={'size': 40, 'class': "form-control"}  ),
			'date': SplitDateTimeWidget(attrs={'size': 40, 'class': "form-control"} ),
		}
	
	def __init__(self, *args, **kwargs):
		# If exclude is there, remove some fields from the Form
		# if kwargs.get('exclude'):
		# 	exclude_list = kwargs.pop('exclude')
		super(AttendanceForm, self).__init__(*args, **kwargs)

		# Removing Form Fields
		# if exclude_list:
		# 	for field in exclude_list:
		# 		del self.fields[field]
		
	def save(self, request, commit=True):
		instance = super(AttendanceForm, self).save(commit=False)
		instance.guser_id = request.user.guser.pk
		if commit:
			instance.save()
		return instance
	

