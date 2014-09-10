# Create your views here.
from minbase.includes import *

from fb.views import *
from googleapp.views import *
from stpros.views import *


# Whereas, it is supposed to be an
# HttpResponse 200 or something else 
# should be decided here.
def main(request):
	
	# funcs dict can be removed
	funcs = {
		"fb_data": fb_data,
		"gp_data": gp_data,
		"get_pts_answers_ajax_call": get_pts_answers_ajax_call,
	}
	
	# print request.POST.getlist()

	# if request.method == "POST":
	# 	return HttpResponse( funcs[request.POST.get('func_to_run')](request) )

	"""
	"""
	if request.method == "POST":
		if request.POST.get('func_to_run') == 'fb_data':
			return HttpResponse( funcs[request.POST.get('func_to_run')](request) )
		if request.POST.get('func_to_run') == 'gp_data':
			print "GP_DATA"
			return HttpResponse( funcs[request.POST.get('func_to_run')](request) )

	
		# if request.POST.get('func_to_run') == 'get_pts_answers':
		# 	return HttpResponse( funcs[request.POST.get('func_to_run')](pts_instance_pk) )
	
	return HttpResponse("Nothing To Show here at the moment")


