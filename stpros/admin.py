from django.db import models

# Create your models here.
from stpros.models import *

from django.contrib import admin

from django.forms import ModelForm
from django.utils.translation import ugettext_lazy as _


### Admin
class PathToSolutionAdmin(admin.ModelAdmin):
	search_fields = ["id",]
	#classes = ["wide", "extrapretty"]
	#readonly_fields = ["date",]
	
	#~fieldsets = [
		#~( None, {'fields': ['title'] } ),
		#~( 'Date Information', {'fields': ['date'], 'classes': ['collapse'] } ),
	#~]
	
	

admin.site.register(PathToSolution, PathToSolutionAdmin)



