# Create your views here.
from minbase.includes import *

from django.core.serializers import serialize

from fb.views import *
from googleapp.views import *
from stpros.views import *
from users.views import *


# Whereas, it is supposed to be an
# HttpResponse 200 or something else 
# should be decided here.
def main(request):
	
	print "main"

	# funcs dict can be removed
	funcs = {
		"fb_data": fb_data,
		"gp_data": gp_data,
		"get_pts_answers_ajax_call": get_pts_answers_ajax_call,
		"fwers_list": fwers_list,
		"ptsD": ptsD,
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
			return HttpResponse( funcs[request.POST.get('func_to_run')](request) )

	if request.method == "GET":
		if request.GET.get('func_to_run') == 'fwers_list':
			data = funcs[request.GET.get('func_to_run')](request)
			# data = serialize("json", data )
			data = json.dumps(data)
			return HttpResponse( data )
		if request.GET.get('func_to_run') == 'ptsD':
			data = funcs[request.GET.get('func_to_run')](request)
			data = json.dumps(data)
			return HttpResponse(data)


	
		# if request.POST.get('func_to_run') == 'get_pts_answers':
		# 	return HttpResponse( funcs[request.POST.get('func_to_run')](pts_instance_pk) )
	
	return HttpResponse("Response from Async Main: Nothing To Show here at the moment")



def fwers_list(request):
	# print "fwers_list"
	fwers = request.user.userprofile.get_followers()
	fwers_user = User.objects.filter(pk__in=fwers.values_list('followers')).select_related('userprofile')
	fwers_user = fwers_user.values('pk', 'email', 'userprofile__avatar')
	# fwers_user = serialize('json', fwers_user, fields=('pk', 'email', 'userprofile__avatar') )
	return list( fwers_user )

def ptsD(request):
	"""Api Function, 
		should only return Truw or False 
		ptsD: PathToSolution Delete

		First; Check whether this Object is the User' own object (i.e. object being created by himself).
		Second: Check Whether he is allowed to Delete? If he is allowed, only then proceed.
	"""
	respo = request.GET.get("response")
	respo = json.loads(respo)
	
	pk = respo.get("pts_id")
	p = PathToSolution.objects.get(pk=pk)

	# Check for Private Key of the User trying to delete & the User who created the Object (pts_id)
	# if p.user.private_key == request.private_key

	ret = p.delete()
	if isinstance(ret, type(None)):
		di = { "pk": pk, "deleted": True}
		return di
	di = {"pk": pk, "deleted": False}
	return di
