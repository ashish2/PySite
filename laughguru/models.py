from django.db import models

# Create your models here.

# Create your models here.
from django.contrib.auth.models import User

from minbase.models import BaseModel
from django.utils.translation import ugettext_lazy as _

# Globals
app_label_q_a = 'laughguru'

class Subject(BaseModel):
	
	name = models.CharField(max_length=1024, null=True, default=None, blank=False)
	def __unicode__(self):
		return unicode(self.name) or u''


class Questions(BaseModel):
	
	subject = models.ForeignKey(Subject)
	# name = models.CharField(max_length=1024, null=True, default=None, blank=False)
	question = models.CharField(max_length=45, null=False, default=None, blank=False)
	opta = models.CharField(max_length=45, null=False, default=None, blank=False)
	optc = models.CharField(max_length=45, null=True, default=None, blank=False)
	optb = models.CharField(max_length=45, null=True, default=None, blank=False)
	optd = models.CharField(max_length=45, null=True, default=None, blank=False)
	optright = models.CharField(max_length=45, null=False, default=None, blank=False)
	orderques = models.CharField(max_length=45, null=False, default=None, blank=False)

	def __unicode__(self):
		return unicode(self.question) or u''


