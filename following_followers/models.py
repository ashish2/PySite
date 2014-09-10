from django.db import models

# Create your models here.

from minbase.includes import *

class Following(models.Model):
	user = models.ForeignKey(User, related_name="by_user")
	following = models.ForeignKey(User, related_name="ff_following") # I am following these Users, These id of Users are being Followed by this User (by_user)


class Followers(models.Model):
	user = models.ForeignKey(User, related_name="of_user") # 
	followers = models.ForeignKey(User, related_name="ff_followers") # These Users are my followers, These id of Users are the Followers of this User (of_user)
	


