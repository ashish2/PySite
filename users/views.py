# Create your views here.

# Only 1 import here, which is the include file, 
# all the other modules are imported in includes.py
from minbase.includes import *

@login_required
def view_user_profile(request, pk):
	#user = request.user
	user = User.objects.filter(pk=pk)
	if not user:
		return HttpResponse("User does not exists")
	user = user[0]
	profile = user.get_profile()
	d = { "user": user , "profile": profile}
	return render_to_response('user_profile.html', d, context_instance=RequestContext(request) )

