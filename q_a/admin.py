from django.db import models

# Create your models here.
from q_a.models import *

from django.contrib import admin

from django.forms import ModelForm
from django.utils.translation import ugettext_lazy as _


### Admin
class PostAdmin(admin.ModelAdmin):
	search_fields = ["id", "title", "content", "slug", "user_ip", "status", "date"]
	classes = ["wide", "extrapretty"]
	
	readonly_fields = ["date",]
	
	#~fieldsets = [
		#~( None, {'fields': ['title'] } ),
		#~( 'Date Information', {'fields': ['date'], 'classes': ['collapse'] } ),
	#~]
	
	
	

class VoteAdmin(admin.ModelAdmin):
	search_fields = ["id", ]
	

admin.site.register(Post, PostAdmin)
admin.site.register(Vote, VoteAdmin)







