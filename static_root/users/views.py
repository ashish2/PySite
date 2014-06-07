# Create your views here.

# Only 1 import here, which is the include file, 
# all the other modules are imported in includes.py
from q_a.includes import *

@login_required
def view_user_profile(request, pk):
	user = request.user
	profile = request.user.get_profile()
	
	print "profile"
	print profile
	
	d = { "user": user , "profile": profile}
	
	return render_to_response('user_profile.html', d, context_instance=RequestContext(request) )
	

