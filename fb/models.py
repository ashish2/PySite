from django.db import models

# Create your models here.
from minbase.includes import *
from django.utils import timezone

from django.utils.translation import ugettext_lazy as _
from accounts.models import UserProfile
from django.contrib.auth.models import Permission, Group
#from minbase.models import BaseModel


class FBUserProfile(BaseModel):
	"""
	If user has provided his fb id, then he will login in from FB,
	if he has same email address & has registered on site & logged in from site email then he can log in from there too.
	"""

	# id
	# user = models.ForeignKey(User, default="", related_name='fb_user')
	user = models.OneToOneField(User, related_name='fb_user')
	fb_id = models.BigIntegerField(_('facebook id'), unique=True)
	#User
	# first_name = models.CharField(_('first name'), max_length=30, blank=True)
	# last_name = models.CharField(_('last name'), max_length=30, blank=True)
	# username = models.CharField(_('username'), max_length=255, blank=True)
	# email = models.EmailField(_('e-mail address'), blank=True)
	# password = models.CharField(_('password'), max_length=128, default=None, null=True, blank=True) # Default None/Null
	# imageurl = models.URLField(max_length=2048, default=None, blank=True, null=True)

	name = models.CharField(_('full name'), max_length=60, blank=True)
	gender = models.CharField(_('gender'), max_length=255, blank=True, null=True)

	#userprofile
	locale = models.CharField( _('locale'), max_length=16, default=None, null=True, blank=True)
	profile_link = models.URLField(max_length=1024, default=None, blank=True, null=True)

	timezone = models.FloatField(default=None, blank=True, null=True)
	accesstoken = models.CharField(max_length=512, verbose_name=_('OAuth token'), default=None, null=True, blank=True)
	response = models.TextField("Most times, Json format with POST or GET from response, A dict", default=None,  blank=True, null=True )
	verified = models.NullBooleanField(_('active'), default=True )
	#userprofile = models.OneToOneField(UserProfile, default=None)
	
	#def __init__(self, *args, **kwargs):
		#super(FBUserProfile, self).__init__(*args, **kwargs)
		#self.fb_id = kwargs.get('id')
		#self.link = kwargs.get('link')
		#self.first_name = kwargs.get('first_name')
		#self.last_name = kwargs.get('last_name')
		#self.name = kwargs.get('name')
		#self.username = kwargs.get('username')
		#self.email = kwargs.get('email')
		#self.gender = kwargs.get('gender')
		#self.locale = kwargs.get('locale')
		#self.link = kwargs.get('link')
		#self.timezone = kwargs.get('timezone')
		#self.verified = kwargs.get('verified')
		#
		
		#self.password = password if password else None
		#self.imageurl = imageurl if imageurl else None
		#self.accesstoken = accesstoken if accesstoken else None
		#self.response = response if response else None
		
	def __unicode__(self):
		return "%s" % self.user.email
	
	def check_password(self, password):
		return True
	
	def is_authenticated(self):
		return True
	
	# def get_profile(self):
	# 	pass
	
	# def userprofile(self):
	# 	return self
	
	#def save(self, *ar, **kw):
		#self.username = self.email
		#super(FBUserProfile, self).save(*ar, **kw)
	


