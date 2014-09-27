from django.db import models

# Create your models here.
from minbase.models import BaseModel
from minbase.includes import *

# class Following(models.Model):
# 	user = models.ForeignKey(User, related_name="by_user")
# 	following = models.ForeignKey(User) # I am following these Users, These id of Users are being Followed by this User (by_user)



# class Followers(models.Model):
# 	user = models.ForeignKey(User, related_name="of_user") # 
# 	followers = models.ForeignKey(User) # These Users are my followers, These id of Users are the Followers of this User (of_user)
	


class Relations(BaseModel):

	followers = models.ManyToManyField(User, related_name="followers") # when i am a follower, follower: myId, following: otherPersonsId
	following = models.ManyToManyField(User, related_name="following") # when i was followed, follower: otherPersonsId, following: myId


class Rel(BaseModel):

	followers = models.ForeignKey(User, related_name="fwers") # when i am a follower, follower: myId, following: otherPersonsId
	following = models.ForeignKey(User, related_name="fwing") # when i was followed, follower: otherPersonsId, following: myId


