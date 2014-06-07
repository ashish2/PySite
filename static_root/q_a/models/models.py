
# Create your models here.

from django.db import models

from django.template.defaultfilters import *
from django.template.defaultfilters import slugify

from django.shortcuts import render, render_to_response

from django.forms import ModelForm

from django.utils.translation import ugettext_lazy as _

from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic

from tagging.models import Tag
from tagging.fields import TagField

from q_a.managers import *


#~from q_a.includes import *

# Globals
app_label_q_a = 'q_a'


# Question Post
class Post(models.Model):
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
	title = models.CharField(max_length=512, null=True, default=None, blank=False)
	content = models.TextField(default=None, blank=True)
	
	# slug = models.CharField(max_length=1000, default=None, blank=True)
	slug = models.SlugField(max_length=128, default=None, blank=True)
	
	# only to indicate whether its a Q or A
	# type = models.EnumField()
	
	# Rows having parent id are by default answers, rows not hving parent_id are Questions
	parent_id = models.ForeignKey("self", null=True, blank=True, default=None, help_text=_("Rows having parent id are by default answers, rows not hving parent_id are Questions"))
	
	date = models.DateTimeField(auto_now_add=True)
	
	user = models.ForeignKey(User)
	
	# This user_ip should go in User table
	# or maybe, what was the IP when this post was made
	user_ip = models.GenericIPAddressField()
	
	# we dont want a boolean field here, since, we may add 2,3,4 and other number depicting some other state
	# values 0-Deactivated, 1-Active, null means untouched
	status = models.IntegerField(default=None, null=True, blank=True)
	
	# Run syncdb, after Uncommenting tags
	# Every post will have multiple tags related to it, on which we can search
	tags = TagField(help_text="Separate different tags with spaces.", default='')
	
	# Images uploaded in the posts
	#images = models.ForeignKey(Images)
	
	
	#~objects = PostManager()
	
	class Meta:
		app_label = app_label_q_a
	
	def __unicode__(self):
		return self.title
	
	def get_tags(self):
		return Tag.objects.get_for_object(self)
	
	def save(self, *args, **kwargs):
		# if not self.id, which means its not an edit of the post but a new creation of the post
		#if not self.id:
		self.slug = slugify(self.title)
		
		# create tags too, if tag field is field, then, loop on their commas & create tag field. for each comma, we'll hv to clie
		# just have to check tags for spaces & stuff, & delete spaces, separate them by commas & put those tags in different rows of tag table
		#self.tags = self.tags
		#tags = self.tags
		
		
		#if kwargs.get('request'):
			#form = myPostForm(request.POST)
			#form.tags = self.cleaned_data["tags"]
			#form.save()
		
		super(Post, self).save(*args, **kwargs)
	
	# Someday
	#~full_name = property("get_query_set")
	
	

class Images(models.Model):
	image = models.ImageField(upload_to="post/")
	# Images uploaded in the posts
	post = models.ForeignKey(Post)
	
	


class Vote(models.Model):
	"""
	Vote up
	vote down
	by_uid
	for_which_question_or_answer(QA_id)
	date
	QA_id(QA object)(1 QA can have many instances of this vote object) (ForeignKey)
	status()act, inactive
	"""
	post = models.ForeignKey(Post)
	by_user = models.ForeignKey(User)
	vote = models.IntegerField() # 1 or -1, positive or negative vote
	date = models.DateTimeField(auto_now_add=True)
	status = models.IntegerField(default=None, null=True, blank=True) # values 0-Deactivated, 1-Active, null-probably untouched yet
	
	class Meta:
		app_label = app_label_q_a
	
	def __unicode__(self):
		return unicode("%s: %s" % (self.post, self.vote) )
	
	


class Share(models.Model):
	"""
	Shares
	This post (post_id) has been shared by this user (user_id) on this date
	"""
	post = models.ForeignKey(Post) # The Post_id that has been shared by the User
	by_user = models.ForeignKey(User) # The User that has shared the Post
	share = models.IntegerField(default=None, null=True) # Share Value, 1 or -1, Shared or has been UnShared back
	date = models.DateTimeField(auto_now_add=True)
	status = models.IntegerField(default=None, null=True, blank=True) # values 0-Deactivated, 1-Active, null-probably untouched yet
	
	class Meta:
		app_label = app_label_q_a
		
	def __unicode__(self):
		return unicode("%s: %s" % (self.post, self.by_user) )
	

# Just for TP, test model
# so that, we can run pysolr with this.
class Cities(models.Model):
	""" Cities table """
	by_user = models.ForeignKey(User, default=1)
	country = models.CharField(max_length=4)
	city_ascii = models.CharField(max_length=100) #accentCity#
	city = models.CharField(max_length=100)
	region = models.CharField(max_length=4)
	population = models.IntegerField(default=0)
	latitude = models.DecimalField(max_digits=10, decimal_places=6)
	longitude = models.DecimalField(max_digits=10, decimal_places=6)
	
	class Meta:
		app_label = app_label_q_a
	

class Wall(models.Model):
	
	
	# STILL TO DO THIS, CHECK
	#~on_user = models.ForeignKey(User),
	#~by_user = models.ForeignKey(User),
	#~
	#~post = models.TextField(null),
	#~
	#~date = models.DateTimeField(),
	#~
	#~#Post  associated with this Replies id, (wall_post_reply table ids associated with this wall_post table id)#
	#~parent_wall_post_id = models.ForeignKey(self, null=True,  ),
	#~
	#~#Either a wall_post (1-post) or a wall_post_reply(2-reply), Denoted as, 1-post, 2-reply#
	#~type = models.tinyint(2) ( null=True ) ,
	#~
	#~#Says the status of the comment, whether, 0-Deleted, 1-Activated, 2-Approved, 3-Unmoderated#
	#~status = models.tinyint(2) ( null=True),
	
	
	
	#print "=============="
	#print "IN q_a Models Wall: "
	#print "Please Check:"
	#print "1] Wall Model"
	#print "2] Include From Root Static Folder, all.css in q_a_bbase.html not coming from Root Static but from Application Static folder, Y?"
	#print "=============="
	
	pass
	


class Follow(models.Model):
	""" 
	Follow object 

	Either user is following a Post, Topic anything,
	else he is not following.

	"""
	
	FIELDTYPES_OF_MODELS = ( 
		( 'U', 'User' ), 
		( 'P', 'Post' ), 
	)
	
	by_user = models.ForeignKey(User)
	follow = models.IntegerField(default=None, null=True) # Follow Value, 1 or -1, Followed or has been UnFollowed back
	
	fieldType = models.CharField(max_length=8, default=None, null=True, help_text="Values: U=>Users , P=>Posts") # Values, U=>Users , P=>Posts
	fieldTypeId = models.IntegerField(default=None, null=True, help_text="Id of the Post of User table, that is represented by above fieldType field")
	
	date = models.DateTimeField(auto_now_add=True)
	status = models.IntegerField(default=None, null=True, blank=True) # Values 0-Deactivated, 1-Active, null-probably untouched yet
	
	# In order to have multiple models in this field, like, Followed this type, like, Followed Post, Followed User etc.
	#content_type = models.ForeignKey(ContentType)
	#object_id = models.PositiveIntegerField()
	#content_object = generic.GenericForeignKey('content_type', 'object_id')
	#-
	
	class Meta:
		app_label = app_label_q_a
		
	#~def __unicode__(self):
		#~return unicode("%s: %d %d" % ( str(self.fieldType), self.by_user, self.follow) )
		#~return unicode("%s: %s" % ( str(self.fieldType), str(self.follow) ) )
	



#class Tag(models.Model):
	"""
	tags

	tags realated to Q (QA_id)(ForeignKey())
	tags related to answers, (QA_id)
	name (tag name, given by user) (CharField() unique)
	slug (tag slug)
	create date
	user who created(User_id)
	date added
	status(inactive, inactive)

	"""
	
	#pass





class Rating():
	"""
	how much is the Rating of an answer or question (good, bad, ugly)
	will be 1-5
	date added
	status(inactive, inactive)

	"""
	pass



class Points():
	"""
	Points of a user 
	gets according to number of questions he answers
	points also given by other users to this user
	starts from 0 - 1000, Million watever...

	points_given_to_user
	number_of_points_(how many points)
	by_user
	for_which_question_or_answer(QA_id)
	date added
	status(inactive, inactive)

	"""
	
	pass



### Managers

class PostManager(models.Manager):
	
	def title_count(self, keyword):
		return self.filter(title__icontains=keyword).count()
	
	
	#def get_full_name(self):
	def get_query_set(self):
		""" returns self title"""
		return super(PostManager, self).get_query_set().filter(title='t')
	
	


