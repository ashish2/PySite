# Create your views here.

from minbase.includes import *
from django.utils.translation import ugettext_lazy as _

from django import forms
from django.contrib.auth.forms import UserCreationForm
from emailusernames.utils import create_user, create_superuser
from emailusernames.forms import user_exists

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
		
		
		


