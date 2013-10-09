# Create your views here.

# Only 1 import here, which is the include file, 
# all the other modules are imported in includes.py
from q_a.includes import *


# @login_required
def userProfile(request, pk):
	user = request.user.get_profile()
	
	
	return HttpResponse(user)
	

# DONE
# @cache_page(60 * 10)
@login_required
def view_all_post(request):
	# posts = Post.objects.filter(~Q(parent_id=None)).order_by("-date")
	posts = Post.objects.filter(Q(parent_id=None)).order_by("-date")
	
	paginator = Paginator(posts, 5)
	
	try:
		page = int(request.GET.get("page", "1"))
	except ValueError:
		page = 1
	
	try:
		posts = paginator.page(page)
	except (InvalidPage, EmptyPage):
		posts = paginator.page(paginator.num_pages)
	
	for post in posts.object_list:
		#~e = post.vote_set.filter( post_id=post.id, by_user=request.user)
		e = None
		e = post.vote_set.filter( post_id=post.id, by_user=request.user.id )
		if e:
			# this means he has voted something
			post.has_voted = e[0].vote
		else:
			# 0, which means he hasn't voted
			post.has_voted = 0
	
	fromUrl = request.get_full_path()
	
	d = dict(posts=posts, fromUrl=fromUrl,)
	return render_to_response('q_a_list.html', d, context_instance=RequestContext(request) )
	#~return HttpResponse(request.user)
	

def view_post_id(request, pk):
	
	post = Post.objects.get(id=pk)
	
	post.vv = post.vote_set.all().filter(vote=1)
	post.vote_count = post.vv.count()
	
	#~for post in posts.object_list:
		#~e = post.vote_set.filter(post_id=post.id)
	
	replies = Post.objects.filter(parent_id=pk).order_by("-date")
	
	d = dict( post = post, replies = replies, )
	return render_to_response('q_a_post_id.html', d, context_instance = RequestContext(request) )
	

# DONE
def show_post_form(request):
	""" Show Post form."""
	#~post = Post.objects.all()
	#d = dict( form=pf, user=request.user, context_instance=RequestContext(request), comments=None, )
	
	#d = dict( form=PostForm(), user=request.user )
	d = dict( form=myPostForm(), user=request.user )
	d.update(csrf(request))
	
	return render_to_response("q_a_post.html", d)
	


# DONE
def add_post(request):
	if request.POST:
		p = request.POST
		
		if p.has_key('content') and p["content"]:
			content = p["content"]
		
		if p.has_key('title') and p["title"]:
			title = p["title"]
		
		ip = get_client_ip(request)
		user = request.user
		#~d.update(csrf(request))
		
		pk = Post.objects.get_or_create( title=title, content=content, user_ip=ip, slug=slug, user_id = user.id)
		
		# True condition, 
		# If everything goes fine, 
		# show the primary key For The Moment
		# Actually supposed to redirect to the page where user came from
	#~return HttpResponseRedirect(reverse("q_a.views.view_post_id", args=[pk]))
		return HttpResponse(pk)
	
	# False condition, Else show the form again
	return HttpResponseRedirect(reverse("q_a.views.show_post_form"))
	


def show_comment_form(request, pk):
	
	pk = Post.objects.get(pk=pk)
	
	fromUrl = request.GET['from']
	d = dict( form=myPostForm( exclude_list=['title'] ), user=request.user , pk=pk.id, fromUrl = fromUrl)
	
	# d = dict( form=PostForm(), user=request.user )
	
	
	d.update(csrf(request))
	return render_to_response("q_a_post.html", d)
	#~return HttpResponse(request.user)
	

def add_comment(request, pk):
	
	if request.POST:
		p = request.POST
		
		if p.has_key('content') and p["content"]:
			content = p["content"]
		
		po = Post.objects.get(pk=pk)
		
		ip = get_client_ip(request)
		user = request.user
		
		#d.update(csrf(request))
		
		pk = Post.objects.get_or_create( title=po.title, content=content, user_ip=ip, user_id = user.id, parent_id=po)
		
		# Redirect to some sort of a next_url here, which will be the same url, 
		# that the user initially came from.
		#~return HttpResponse(pk)
		f =request.GET['from']
		return HttpResponseRedirect(f)
	
	# else, show the same form again
	# If its not a post, then just redirect to the comment form again
	return HttpResponseRedirect(reverse("q_a.views.show_comment_form"))
	

#@login_required
def vote(request, pk, vote):
	"""VOTES: 
	Will get the Post id, and +1 or -1 as vote"""
	
	vote = int(vote)
	
	p = Post.objects.get(pk=pk)
	
	# Deactivated for the moment
	status = static['vote_field_default_status']
	
	u = static['root_user_id']
	
	# Login required, if we put it in the descriptor, we dont have to use this if condition,
	# using only FTM
	if request.user.id:
		#d = dict( by_user=request.user, vote=vote, status=status )
		d = dict( by_user=request.user, vote=vote, status=status )
		
		# by default 1 user can vote to a post_id only once
		obj, cr = p.vote_set.get_or_create(**d)
		
		# If an object was created
		if cr:
			pass
		# else, if it was not created
		else:
			pass
		
		#~
		#~try:
			#~referer = request.META['HTTP_REFERER']
		#~except:
			#~referer = urlsplit(referer, 'http', False)[2]
		#~else:
			#~referer = 'No'
		
		
		f =request.GET['from']
		
		return HttpResponseRedirect(f)
	else:
		return HttpResponse('Please Login here.')
	

# Share
def share(request, pk):
	
	# Deactivated for the moment
	status = static['vote_field_default_status']
	
	s = Share.objects
	obj, cr = s.get_or_create( post_id=pk, by_user=request.user, status=status)
	
	# If an object was created
	if cr:
		pass
	# else, if it was not created
	else:
		pass
	
	return HttpResponse(cr)
	

# Login for the moment
def login_view(request):
	username = request.POST.get('username', '')
	password = request.POST.get('password', '')
	user = auth.authenticate(username=username, password=password)
	if user is not None and user.is_active:
		# Correct password, and the user is marked "active"
		auth.login(request, user)
		# Redirect to a success page.
		return HttpResponseRedirect("/account/loggedin/")
	else:
		# Show an error page
		return HttpResponseRedirect("/account/invalid/")
		

def logout_view(request):
	auth.logout(request)
	# Redirect to a success page.
	return HttpResponseRedirect("/account/loggedout/")
	




# Actual login shud be somthing like this, based on Email loging in
#~def login_view(request):
	#~if request.POST:
		#~email = UserProfile.objects.get(email=request.POST.get('email'))
		#~if email:
			#~username = request.POST.get('username')
			#~
			#~if email.user_set.get == username:
				#~pass
		#~


def random(request):
	st = ''
	#~for e in request.session.__dict__:
		#~st += str(e) + '<br />'
		
	#~for e in request.session.__dict__:
		#~st += str(e) + '<br />'
	
	#~st += '<br />'
	
	#~for e in request.items():
		#~st += str(e) + '<br />'
	
	# t = type(request)
	
	#~r = dir(request.session)
	
	
	# Set AUTH_PROFILE_MODULE in settings then see this
	#~prof = request.user.get_profile()
	#~email = prof.email
	
	#~return HttpResponse( request._cookies )
	#~return HttpResponse( request.session )
	return HttpResponse( st )
	#~return HttpResponse( r )
	#~return HttpResponse( t )
	

