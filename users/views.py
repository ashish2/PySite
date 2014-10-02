# Create your views here.

# Only 1 import here, which is the include file, 
# all the other modules are imported in includes.py
from minbase.includes import *

def ret_first_elem_of_a_list_tup(el):
	return el[0]

@login_required
def view_user_profile(request, pk):
	# User or FBUser or TwitterUser, request.user, which?
	# how will you join FBUser & PTS table id?
	#user = request.user
	user = User.objects.filter(pk=pk)

	if not user:
		return HttpResponse("User does not exists")

	user = user[0]
	profile = user.get_profile()
	user_pts_questions = PathToSolution.objects.filter(user=user, parent_id=None)
	user_pts_answers = PathToSolution.objects.filter(user=user).filter(~Q(parent_id=None))
	fromUrl = request.get_full_path()

	fwers = map(ret_first_elem_of_a_list_tup, user.fwing.values_list('followers_id') )
	user.followers_list = fwers
	d = { "user": user , "profile": profile, "user_pts_questions": user_pts_questions, "user_pts_answers": user_pts_answers, "fromUrl":fromUrl}

	return render_to_response('user_profile.html', d, context_instance=RequestContext(request) )


@login_required
def edit_user_profile(request, pk):

	u = User.objects.get(email=request.user.email)
	user_form = UserForm(instance=u)
	user_profile_form = UserProfileForm(instance=u.userprofile)

	if request.method == 'POST':
		user_form = UserForm(request.POST, instance=u)
		up = UserProfile.objects.get(user=request.user)
		user_profile_form = UserProfileForm(request.POST, request.FILES, instance=up)

		if user_form.is_bound and user_profile_form.is_bound:
			if user_form.is_valid() and user_profile_form.is_valid():
				user_form.instance.first_name = user_form.cleaned_data.get('first_name')
				user_form.instance.last_name = user_form.cleaned_data.get('last_name')
				user_form.save(request)

				# Even if you comment out below 'avatar' line, it still saves the pic
				user_profile_form.instance.avatar = user_profile_form.cleaned_data.get('avatar')
				user_profile_form.instance.biography = user_profile_form.cleaned_data.get('biography')
				user_profile_form.save(request)

			else:
				print "Form Invalid"
				print user_form.errors
				print user_profile_form.errors
		else:
			print "No data received in form"
	else:
		print "Some problem occurred while submitting the form"
	
	fromUrl = request.get_full_path()

	d = dict( user_form = user_form , user_profile_form = user_profile_form, )

	return render_to_response( 'acc_some_post_form.html', d, context_instance=RequestContext(request) )


def get_user(pk):
	return User.objects.get(pk=pk)

@login_required
def get_followers_list(request, pk):
	"""get users followers"""
	user = get_user(pk)
	fwers = user.fwers.all()
	# return HttpResponse(fwers)
	return fwers

@login_required
def get_following_list(request, pk):
	"""get users followers"""
	user = get_user(pk)
	fwing = user.fwing.all()
	# return HttpResponse(fwing)
	return fwing




# To handle uploaded files
# def handle_uploaded_file(f):
#     with open('uploads/avatar/name.txt', 'wb+') as destination:
#         for chunk in f.chunks():
#             destination.write(chunk)
