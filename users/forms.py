from django import forms

# Create your models here.

from minbase.includes import *
from emailusernames.forms import *



@login_required
# DONE
def user_edit_form(request):
	""" Show Post form. """
	#~post = Post.objects.all()
	#d = dict( form=pf, user=request.user, context_instance=RequestContext(request), comments=None, )
	
	#d = dict( form=PostForm(), user=request.user )
	d = dict( form=EmailUserChangeForm(), user=request.user )
	d.update(csrf(request))
	
	#print RequestContext(request)
	
	return render_to_response("user_edit_form.html", d, context_instance = RequestContext(request))
	


