from django.db import models

# Create your models here.
from minbase.includes import *
from django.utils import timezone

from django.contrib.auth.models import User

from minbase.models import BaseModel
from django.utils.translation import ugettext_lazy as _


# Create models &
# thier modelforms forms
# create a login, checking for an arbit value like, request.session.blah if set then login else logged out,
# check, for a few, emails & disallow them to login, like, all@samhita.org etc
# create a tastypie API

# Samhita Assignment
# Project 1 .Create a Timesheet web app that does the following
# 1. Authenticates Users through google login
# 2. Allows users only from @samhita.org to login
# 3. Allows filtering of by certain defiend usernames "mail, admin, all"

# 4. After authentication stores user google plus image, Name into the Database - First time only
# 	a. Create primary key on Db
# 	b. Create designation column on Db 

# 5. redirect User to Form :
# 	a. Number of hours worked on the date
# 	b. Choose differnt dates in the month to enter data
# 	c. See previously entered data and be able to edit this data
# 6. Store the information with date-timestamp in database

# 7. Create Admin backend that allows admin to set employee Designation for each registered employee, Activate/deactivate employee login.
# 8. Create a rest API that out put above information in JSON
# 	a. List of all registered employees
# 	b. List of all employees and total number of entries in a month
# Please use the bootstrap Frontend framework to create this application


app_label_q_a = 'googleapp'


class Guser(BaseModel):
	"""
	google+ user
	"""
	"""
	If user has provided his fb id, then he will login in from FB,
	if he has same email address & has registered on site & logged in from site email then he can log in from there too.
	"""
	user = models.OneToOneField(User , related_name="guser")
	gid = models.CharField(_('Google plus id'), max_length=60, unique=True )
	name = models.CharField(_('full name'), max_length=60, blank=True)
	gender = models.CharField(_('gender'), max_length=255, blank=True, null=True)
	locale = models.CharField( _('locale'), max_length=16, default=None, null=True, blank=True)
	profile_link = models.URLField(max_length=1024, default=None, blank=True, null=True)
	timezone = models.FloatField(default=None, blank=True, null=True)
	accesstoken = models.CharField(max_length=512, verbose_name=_('OAuth token'), db_index=True, default=None, null=True, blank=True)
	response = models.TextField("Most times, Json format with POST or GET from response, A dict", default=None,  blank=True, null=True )
	verified = models.NullBooleanField(_('active'), default=True )
	designation = models.CharField(_('Designation'), max_length=30, blank=True)
	
	class Meta:
		app_label = app_label_q_a
	
	def __unicode__(self):
		return unicode("%s: %s: %s" % (self.gid, self.name, self.user.email) ) or u''
	
	def check_password(self, password):
		return True
	
	def is_authenticated(self):
		return True
	
	# def get_profile(self):
	# 	pass
	
	# def userprofile(self):
	# 	return self
	

# class GuserProfile(BaseModel):
# 	user = models.OneToOneField(User)
# 	avatar = models.ImageField(upload_to="uploads/avatar_googleapp", default="", blank=True )
# 	biography = models.TextField(default="", blank=True)
# 	response = models.TextField( _("Most times, Json format with POST or GET from response, A dict"), default=None,  blank=True, null=True )
		
# 	def __unicode__(self):
# 		return self.user.username


class Attendance(BaseModel):
	guser = models.ForeignKey(Guser)
	pub_date = models.DateTimeField(_('Date Published') )
	hours = models.IntegerField(_('Hours') )

	def __unicode__(self):
		return unicode( ("%s - %s" ) % (self.pub_date, self.hours) )

	# class Meta:
	# 	app_label = app_label_q_a


