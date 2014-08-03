# Create your views here.

from minbase.includes import *

def fb_login(request):
	
	d = {"ASYNC_URL": ASYNC_URL, }
	print d
	return render_to_response( 'fb_login.html', d, context_instance=RequestContext(request) )


def privacypolicy(request):
	d = {}
	return render( request, 'privacypolicy.html', d, context_instance=RequestContext(request) )
