# Create your views here.

from minbase.includes import *

def fb_login(request):
	
	d = {"ASYNC_URL": ASYNC_URL, }
	print d
	return render_to_response( 'fb_login.html', d, context_instance=RequestContext(request) )



def about(request):
	d = {}
	return render( request, 'about.html', d, context_instance=RequestContext(request) )

def team(request):
	d = {}
	return render( request, 'team.html', d, context_instance=RequestContext(request) )

def contact(request):
	d = {}
	return render( request, 'contact.html', d, context_instance=RequestContext(request) )

def terms(request):
	d = {}
	return render( request, 'terms.html', d, context_instance=RequestContext(request) )

def privacypolicy(request):
	d = {}
	return render( request, 'privacypolicy.html', d, context_instance=RequestContext(request) )


