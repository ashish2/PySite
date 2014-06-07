"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

# Pysolr
#from __future__ import print_function
#import pysolr
# Pysolr/

# Working Fine
# url = 'http://localhost:8983/solr/collection1'
# q=city_ascii:burzina
# Working Fine-

url = 'http://localhost:8983/solr/custom'
#q=*%3A*&wt=json&indent=true

def solr_example():
	solr = pysolr.Solr('http://localhost:8983/solr/', timeout=10)
	# How you'd index data.
	solr.add([
		{
			"id": "doc_1",
			"title": "A test document",
		},
		{
			"id": "doc_2",
			"title": "The Banana: Tasty or Dangerous?",
		},
	])
	# You can optimize the index when it gets fragmented, for better speed.
	solr.optimize()
	# Later, searching is easy. In the simple case, just a plain Lucene-style
	# query is fine.
	results = solr.search('bananas')
	# The ``Results`` object stores total results found, by default the top
	# ten most relevant results and any additional data like
	# facets/highlighting/spelling/etc.
	print("Saw {0} result(s).".format(len(results)))
	# Just loop over it to access the results.
	for result in results:
		print("The title is '{0}'.".format(result['title']) )
	# For a more advanced query, say involving highlighting, you can pass
	# additional options to Solr.
	results = solr.search('bananas', **{
		'hl': 'true',
		'hl.fragsize': 10,
		}
	)
	
	# You can also perform More Like This searches, if your Solr is configured
	# correctly.
	similar = solr.more_like_this(q='id:doc_2', mltfl='text')
	# Finally, you can delete either individual documents...
	solr.delete(id='doc_1')
	# ...or all documents.
	solr.delete(q='*:*')
	

def search_solr():
	pass

def serialize_it():
	from django.core import serializers
	i = Post.objects.get(pk=1)
	post_json = serializers.serialize('json', i)
	li = []
	li.append(post_json)
	
	

# Start writing search functionality here,
# search the cities table etc.
class PysolrSearch():
	def test_basic_addition(self):
		"""
		Tests that 1 + 1 always equals 2.
		"""
		self.assertEqual(1 + 1, 2)
		
		
	
