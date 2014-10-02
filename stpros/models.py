# Path to Problem Solving # Steps to Problem Solving

from django.db import models
# Create your models here.
from django.contrib.auth.models import User

from minbase.models import BaseModel
from django.utils.translation import ugettext_lazy as _

# Globals
app_label_q_a = 'stpros'

class PathToSolution(BaseModel):
	
	problem = models.CharField(max_length=1024, null=True, default=None, blank=False)
	answer = models.TextField()
	user = models.ForeignKey(User, help_text=_("The user who posted this answer"))
	slug = models.SlugField(max_length=128, null=True, default=None, blank=True)
	parent_id = models.ForeignKey("self", null=True, blank=True, default=None, help_text=_("Rows having parent id are by default answers, rows not hving parent_id are Questions"))
	
	# Can be implemented Later
	# Likes
	#likes = generic.GenericForeignKey(q_a.models.like)
	# Ratings
	#ratings = generic.GenericForeignKey(q_a.models.ratings)
	# Comments on this page
	#comments = generic.GenericForeignKey(q_a.models.comments)
	# tags on the answer
	#tags = models.TagField()
	
	def __unicode__(self):
		return unicode(self.problem) or u''

	def get_pts_answers(self):
		"Takes an pts instance id, returns answers"
		replies = PathToSolution.objects.filter(parent_id__pk=self.id).order_by("-date")
		return replies
		

	def get_votes(self):
		pass

	def get_sum_of_votes():
		pass

	def is_user_in_votes():
		pass

	def get_vote_for_pts(self):
		pts_instance = PathToSolution.objects.get(pk=pts_instance_pk)
		votes = pts_instance.vote_set.filter( pts_id=pts_instance_pk, user=request.user.id )
		return votes

	

# To be added and synced
class Vote(BaseModel):
	"""
	Vote up
	vote down
	by_uid
	for_which_question_or_answer(QA_id)
	date
	QA_id(QA object)(1 QA can have many instances of this vote object) (ForeignKey)
	status()act, inactive
	"""
	pts = models.ForeignKey(PathToSolution)
	user = models.ForeignKey(User , related_name="pts_vote_by_user")
	vote = models.IntegerField( help_text=_("1 or -1, positive or negative vote") )
	
	class Meta:
		app_label = app_label_q_a
	
	def __unicode__(self):
		return unicode("%s: %s" % (self.pts, self.vote) ) or u''
	

class Favorite(BaseModel):
	pts = models.ForeignKey(PathToSolution)
	user = models.ForeignKey(User , related_name="fav_by_user")
	#fave = models.IntegerField( help_text=_("1 or -1, positive or delete fav"), default=1 )
	
	class Meta:
		app_label = app_label_q_a
	
	def __unicode__(self):
		return unicode("%s: %s" % (self.pts, self.user) ) or u''
	


