from django.db import models

# Create your models here.

from minbase.includes import *
from django.utils.translation import ugettext_lazy as _

class Tutsplus(BaseModel):
	tutUrl = models.URLField()
	tutTitle = models.CharField(max_length=600)
	tutLength = models.FloatField()
	# Author' Table
	authorName = models.CharField(max_length=100)
	authorBio = models.TextField()
	authorAboutLink = models.URLField()
	numberOfLessons = models.PositiveSmallIntegerField()
	# Categories Table
	categories = models.TextField(help_text=_("Storing a dict as a string, time being"))

	courseDescription = models.TextField()
	courseFees = models.DecimalField(max_digits=10, decimal_places=2)
	courseFeeLink = models.URLField(max_length=300)
	courseStartDate = models.DateTimeField()

	@property
	def price(self):
		return "$%s" % self.courseFees






