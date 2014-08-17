# Create your views here.

from minbase.includes import *
from django.utils.translation import ugettext_lazy as _

from django import forms
from django.contrib.auth.forms import UserCreationForm
from emailusernames.utils import create_user, create_superuser
from emailusernames.forms import user_exists
from django.forms import ModelForm

from accounts.models import UserProfile

class RegistrationForm(UserCreationForm):

	username = forms.RegexField(label=_("Email"), max_length=30,
        regex=r'^[\w.@+-]+$',
        help_text = _("Required. 30 characters or fewer. Letters, digits and "
                      "@/./+/-/_ only."),
        error_messages = {
            'invalid': _("This value may contain only letters, numbers and "
                         "@/./+/-/_ characters.")})
	
	#class Meta(UserCreationForm.Meta):
		#model = User
		#fields = ("username",)
		
		#widgets = {
			#'username': TextInput(attrs={'size': 40, 'class': "form-control"}  ),
			#'password1': TextInput(attrs={'size': 40, 'class': "form-control"}  ),
			#'password2': TextInput(attrs={'size': 40, 'class': "form-control"}  ),
		#}
		
	
	def __init__(self, *args, **kwargs):
		super(RegistrationForm, self).__init__(*args, **kwargs)
		# Y this working & Meta.widgets not working
		for i in self.fields:
			self.fields[i].widget.attrs['class'] = 'form-control'
			#self.fields[i].widget.attrs['placeholder'] = 'form-control'
			self.fields[i].widget.attrs['placeholder'] = self.fields[i].label.__dict__['_proxy____args'][0]


class UserForm(ModelForm):
	"""docstring for UserForm"""
	class Meta:
		model = User
		fields = ( 'first_name',  'last_name' )

	def __init__(self, *args, **kwargs):
		"""
		# Y cant we access and change a python Class' attributes & methods when the class is raw, before initializing an object,
		# y are we supposed to access & change them only after initializing the class object.
		"""
		# print "self"
		# print UserForm.Meta
		# print dir(UserForm)
		if kwargs.get('fields'):
			fields = kwargs.get('fields')

		super(UserForm, self).__init__(*args, **kwargs)
		self.fields['first_name'].widget.attrs['class'] = 'form-control'
		self.fields['last_name'].widget.attrs['class'] = 'form-control'

	def save(self, request, commit=True):
		instance = super(UserForm, self).save(commit=False)
		instance.user = request.user
		if commit:
			instance.save()
		return instance


class UserProfileForm(ModelForm):
	"""docstring for UserProfileForm"""
	
	class Meta:
		model = UserProfile
		exclude = ( 'is_active', 'user', )

	def __init__(self, *args, **kwargs):
		super(UserProfileForm, self).__init__(*args, **kwargs)
		self.fields['biography'].widget.attrs['class'] = 'form-control'		
		# if request in args:
		# 	if user in request:
		# 		self.user = request.user.pk

	def save(self, request, commit=True):
		instance = super(UserProfileForm, self).save(commit=False)
		if commit:
			instance.save()
		return instance

		
