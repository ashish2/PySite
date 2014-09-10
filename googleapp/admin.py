from django.db import models

# Create your models here.
from minbase.includes import *

from django.contrib import admin

from django.forms import ModelForm
from django.utils.translation import ugettext_lazy as _

from googleapp.models import *

### Admin
class GuserAdmin(admin.ModelAdmin):
	search_fields = ["id", "name", ]
	classes = ["wide", "extrapretty"]
	
	# readonly_fields = ["date",]
	
	#~fieldsets = [
		#~( None, {'fields': ['title'] } ),
		#~( 'Date Information', {'fields': ['date'], 'classes': ['collapse'] } ),
	#~]
	
	
# class GuserProfileAdmin(admin.ModelAdmin):
	# search_fields = ["id", "name", ]
	# classes = ["wide", "extrapretty"]
	# pass
	
	

class AttendanceAdmin(admin.ModelAdmin):
	search_fields = ["id", ]
	

admin.site.register(Guser, GuserAdmin)
# admin.site.register(GuserProfile, GuserProfileAdmin)
admin.site.register(Attendance, AttendanceAdmin)







