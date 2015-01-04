# Create your views here.

from q_a.staticvals import *
from minbase.includes import *
from laughguru.forms import *

from laughguru.models import *


def read(request, pk):
	post = Questions.objects.get(pk=pk)

	fromUrl = request.get_full_path()

	if request.method == 'POST':
		post.awesome = False
		if request.POST.get('answer') and request.POST.get('answer').lower() == post.optright.lower():
			post.awesome = True

	d = dict( some_id = post, fromUrl=fromUrl, pk=pk, q_count=Questions.objects.count() )
	return render_to_response('lg_read_some_particular_id.html', d, context_instance = RequestContext(request) )

def result(request):
	# post = Questions.objects.get(pk=pk)

	# fromUrl = request.get_full_path()

	# if request.method == 'POST':
	# 	post.awesome = False
	# 	if request.POST.get('answer') and request.POST.get('answer').lower() == post.optright.lower():
	# 		post.awesome = True

	# d = dict( some_id = post, fromUrl=fromUrl, pk=pk, q_count=Questions.objects.count() )
	d = dict()
	return render_to_response('lg_result.html', d, context_instance = RequestContext(request) )


