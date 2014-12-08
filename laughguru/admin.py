from django.db import models

# Create your models here.
from laughguru.models import *

from django.contrib import admin

from django.forms import ModelForm
from django.utils.translation import ugettext_lazy as _


### Admin
# class Subject(admin.ModelAdmin):
# 	search_fields = ["id",]
# 	#classes = ["wide", "extrapretty"]
# 	#readonly_fields = ["date",]
	
# 	#~fieldsets = [
# 		#~( None, {'fields': ['title'] } ),
# 		#~( 'Date Information', {'fields': ['date'], 'classes': ['collapse'] } ),
# 	#~]
	

# class Questions(admin.ModelAdmin):
# 	search_fields = ["id",]

class SubjectAdmin(admin.ModelAdmin):
	search_fields = ["id"]

class QuestionsAdmin(admin.ModelAdmin):
	search_fields = ["id"]

admin.site.register(Subject, SubjectAdmin)
admin.site.register(Questions, QuestionsAdmin)



