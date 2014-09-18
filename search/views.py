# Create your views here.

from minbase.includes import *


def normalize_query(query_string, findterms=None, normspace=None ):

	if not findterms:
		findterms=re.compile(r'"([^"]+)"|(\S+)').findall

	if not normspace:
		normspace=re.compile(r'\s{2,}').sub

	"""Splits the query string in individual keywords, getting rid of unnecessary spaces 
		and grouping quoted words together.
		Example:
			normalize_query('some random words "with quotes" and spaces')
			['some', 'random', 'words', 'with quotes', 'and', 'spaces']
	"""
	return [ normspace(' ', (t[0] or t[1]).strip()) for t in findterms(query_string) ]

def get_query(query_string, search_fields):
	"""Returns a query that is a combination of Q objects.
	That combination aims to search keywords within a model by testing the
	given search fields"""
	query = None # Query to search for every search term
	terms = normalize_query(query_string)
	for term in terms:
		or_query = None # Query to search for a given term in each field
		for field_name in search_fields:
			q = Q(**{"%s__icontains" % field_name: term})
			if or_query is None:
				or_query = q
			else:
				or_query = or_query | q
		
		if query is None:
			query = or_query
		else:
			query = query & or_query

	print "query"
	print query

	return query

def search(request):
	query_string = ''
	found_entries = None
	d = {}
	if ( 'q' in request.GET ) and request.GET.get('q').strip():
		query_string = request.GET.get('q')
		pts_query = get_query( query_string, ['problem', 'answer'] )

		found_entries = PathToSolution.objects.filter(pts_query).order_by('-date')
		somelist = found_entries

		d = { 'query_string': query_string, 'somelist': somelist}

	return render_to_response('se_some_list.html', d, context_instance = RequestContext(request) )


def main(request):
	print "request.GET"
	print request.GET.get("q")

	return HttpResponse("So, here we are, starting probably 1 of the most legendary modules that we will ever write and build, called: `The Search`.")




