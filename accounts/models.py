from django.db import models

# Create your models here.

from django.db.models.signals import post_save
from django.contrib.auth.models import User

# Globals
app_label_q_a = 'accounts'

"""
UserProfile table


"""
#~class UserProfile(models.Model):
	#~user = models.ForeignKey(User, unique=True)
	#~email = models.EmailField(max_length=254, help_text=_("User Email") )
	#~date = models.DateTimeField(auto_now_add=True, help_text=_("Date of registeration") )
	#~status = models.IntegerField(default=None, null=True, blank=True, help_text=_("Values 0-Deactivated, 1-Active, null-probably") ) # Values 0-Deactivated, 1-Active, null-probably
	#~
	#~class Meta:
		#~app_label = app_label_q_a
		#~
	#~def __unicode__(self):
		#~return unicode("%s: %s" % (self.post, self.by_user) )
	#~

# User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])

class UserProfile(models.Model):
	user = models.OneToOneField(User)
	avatar = models.ImageField(upload_to="uploads/avatar", default="", blank=True)
	biography = models.TextField(default="", blank=True)
	
	
	def __unicode__(self):
		return self.user.username
	

def create_user_profile( sender, instance, created, **kwargs):
	"""Created the UserProfile when a new User is saved"""
	if created:
		profile = UserProfile()
		profile.user = instance
		profile.save()

post_save.connect(create_user_profile, sender=User)





