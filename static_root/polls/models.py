from django.db import models

# Create your models here.

import datetime
from django.utils import timezone
from django.contrib import admin


class Poll(models.Model):
	question = models.CharField(max_length=200)
	pub_date = models.DateTimeField('Date Published')
	
	def __unicode__(self):
		return self.question
	
	def was_published_recently(self):
		return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
	
	# Adding below, 
	# just to show it in a particular way in the admin site for was_published_recently
	was_published_recently.admin_order_field = 'pub_date'
	was_published_recently.boolean = True
	was_published_recently.short_description = 'Published recently?'
	
	def hello_world(self):
		return "Hello, World!"
	
	
	

class Choice(models.Model):
	choice = models.CharField(max_length=200)
	votes = models.IntegerField()
	poll = models.ForeignKey(Poll)
	
	def __unicode__(self):
		return self.choice
	
	

### Inlines

#class ChoiceInline(admin.StackedInline):
class ChoiceInline(admin.TabularInline):
	model = Choice
	extra = 3
	

### Admin
class PollAdmin(admin.ModelAdmin):
	
	# For fields in the admin form
	fieldsets = [
		( 'Question you can put.', {'fields': ['question'] } ), 
		('Date information', {'fields': ['pub_date'], 'classes': ['collapse']} ),
	]
	
	# There are quite few
	# inherent django Admin class properties
	# like
	# list_display, list_filter, search_fields, date_hierarchy, inlines
	
	# for List page (change list page)
	list_display = ["id", "question", "pub_date", "was_published_recently"]
	
	# For filters on the right
	list_filter = ["pub_date"]
	
	# For search
	search_fields = ["question"]
	
	# For hierarchical navigation at the top, will be according to the `pub_date` field 
	date_hierarchy = "pub_date"
	
	# For inlines related to the foreignkey of this object (foreignkeys of this object)
	inlines = [ChoiceInline]
	

class ChoiceAdmin(admin.ModelAdmin):
	list_display = ["id", "choice", "votes", "poll"]
	


