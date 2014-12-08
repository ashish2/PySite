from django.db import models

# Create your models here.
from tutsplus.models import *

from django.contrib import admin

from django.forms import ModelForm
from django.utils.translation import ugettext_lazy as _


### Admin
class TutsplusAdmin(admin.ModelAdmin):
	search_fields = ["id",]
	#classes = ["wide", "extrapretty"]
	#readonly_fields = ["date",]
	
	#~fieldsets = [
		#~( None, {'fields': ['title'] } ),
		#~( 'Date Information', {'fields': ['date'], 'classes': ['collapse'] } ),
	#~]
	
	


admin.site.register(Tutsplus, TutsplusAdmin)



