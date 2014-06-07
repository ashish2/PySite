from django.db import models

# Create your models here.

from django.forms import ModelForm
from django.utils.translation import ugettext_lazy as _

"""
So there is a Page,
there are Posts (QA),
there will be Vote up/Vote down on posts,
there will be Tags of each posts,
there are Users,

so objects are,
Posts,
Votes,
Tags,
Users,
Like/Unlike or Emotion object(1-Like, 2-Unlike, 3-Hot, 4-Beautiful) for each post

"""

"""
Question & Answer table is object:::

question / answer/ post
title
description/text/content,
slug,
//votes_id - votes (up, down)(related to each answer, related to question also) (OBJECT)
parent_id(self)
type ( Q(1) if Question parent_id will be null, A(2) if Answer parent_id will be question_id (SELF OBJECT))(as it is goin to be the same table for q&a, and A will have the id of the question )
user_id(who created) (OBJECT) ForeiKey(User)
time_created,
status (0-deactive, 1-active, )
user_ip (IPfield())
"""
class Posts(models.Model):
	title = models.CharField(max_length=512, default=None, blank=False)
	content = models.TextField(default=None, blank=True)
	
	# slug = models.CharField(max_length=1000, default=None, blank=True)
	slug = models.SlugField(max_length=128, default=None, blank=True)
	
	# only to indicate whether its a Q or A
	# type = models.EnumField()
	
	# Rows having parent id are by default answers, rows not hving parent_id are Questions
	parent_id = models.ForeighKey(self, null=True, help_text=_("Rows having parent id are by default answers, rows not hving parent_id are Questions"))
	
	date = models.DatetimeField(auto_now_add=True)
	
	user = models.ForeignKey(User)
	
	# This user_ip should go in User table
	# or maybe, what was the IP when this post was made
	user_ip = models.GenericIPAddressField()
	
	# we dont want a boolean field here, since, we may add 2,3,4 and other number depicting some other state
	status = models.IntegerField(default=None, null=True) # values 0-Deactivated, 1-Active
	
	
	def __unicode__(self):
		return self.title
	
	


"""
Vote up
vote down
by_uid
for_which_question_or_answer(QA_id)
date
QA_id(QA object)(1 QA can have many instances of this vote object) (ForeignKey)
status()act, inactive
"""
class Votes():
	post = models.ForeignKey(Posts)
	by_user = models.ForeignKey(User)
	vote = models.IntegerField()
	date = models.DatetimeField(auto_now_add=True)
	status = models.IntegerField(default=None, blank=True) # values 0-Deactivated, 1-Active
	
	def __unicode__(self):
		return unicode("%s: %s" % (self.post, self.vote) )
	
	



"""
tags

tags realated to Q (QA_id)(ForeignKey())
tags related to answers, (QA_id)
name (tag name, given by user) (CharField() unique)
slug (tag slug)
create date
user who created(User_id)
status(inactive, inactive)

"""
class Tags(models.Model):
	pass




"""
how much is the Rating of an answer or question (good, bad, ugly)
will be 1-5

"""
class Rating():
	pass


"""
Points of a user 
gets according to number of questions he answers
points also given by other users to this user
starts from 0 - 1000, Million watever...

points_given_to_user
number_of_points_(how many points)
by_user
for_which_question_or_answer(QA_id)
date

"""
class Points():
	pass
