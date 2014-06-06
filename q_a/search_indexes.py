import datetime
from haystack import indexes
from myapp.models import Note


class NoteIndex(indexes.SearchIndex, indexes.Indexable):
	text = indexes.CharField(document=True, use_template=True)
	by_user = indexes.ForeignKey(model_attr='user')
	pub_date = indexes.DateTimeField(model_attr='pub_date')
	country = indexes.CharField(max_length=4)
	city_ascii = indexes.CharField(max_length=100) #accentCity#
	city = indexes.CharField(max_length=100)
	region = indexes.CharField(max_length=4)
	population = indexes.IntegerField(default=0)
	latitude = indexes.DecimalField(max_digits=10, decimal_places=6)
	longitude = indexes.DecimalField(max_digits=10, decimal_places=6)
	
	def get_model(self):
		return Note
	
	def index_queryset(self, using=None):
		"""Used when the entire index for model is updated."""
		return self.get_model().objects.filter(pub_date__lte=datetime.datetime.now())
		
