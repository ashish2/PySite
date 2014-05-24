# Create your views here.

# Only 1 import here, which is the include file, 
# all the other modules are imported in includes.py
from q_a.includes import *

# Search
# Pysolr
#import search
# Pysolr/

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
		# this means he has voted something 			# 0, which means he hasn't voted
		post.has_voted = e[0].vote if e else 0
		
		e = None
		e = post.share_set.filter( post_id=post.id, by_user=request.user.id )
		# this means he has voted something 	# 0, which means he hasn't voted
		post.has_shared = e[0].share if e else 0
		
		#post.vote_count = post.vote_set.count()
		post.vote_count = post.vote_set.aggregate(Sum('vote'))['vote__sum'] or 0
	
	fromUrl = request.get_full_path()
	
	
	d = dict(posts=posts, fromUrl=fromUrl,)
	return render_to_response('q_a_list.html', d, context_instance=RequestContext(request) )
	#~return HttpResponse(request.user)
	

def view_post_id(request, pk, slug):
	
	post = Post.objects.get(id=pk)
	
	# Getting whether the logged in user is following this Question post
	# fieldType, typ = 'P' FTM , as this is the Post function, over here we will only view Posts
	typ = 'P'
	
	#~follow = Follow.objects.get( by_user=request.user, fieldTypeId=pk, fieldType=typ )
	follow = Follow.objects.filter( by_user=request.user, fieldTypeId=pk, fieldType=typ )
	
	post.vv = post.vote_set.all().filter(vote=1)
	post.vote_count = post.vv.count()
	
	#~for post in posts.object_list:
		#~e = post.vote_set.filter(post_id=post.id)
	
	replies = Post.objects.filter(parent_id=pk).order_by("-date")
	
	i = None
	for r in replies:
		i = r.vote_set.filter(by_user_id=request.user)
		if i:
			r.has_voted = i[0].vote
		else:
			r.has_voted = 0
		
	
	fromUrl = request.get_full_path()
	
	d = dict( post = post, replies = replies, fromUrl=fromUrl, follow=follow)
	
	return render_to_response('q_a_post_id.html', d, context_instance = RequestContext(request) )
	

#========

# DONE
def show_post_form(request):
	''' Show Post form. '''
	#~post = Post.objects.all()
	#d = dict( form=pf, user=request.user, context_instance=RequestContext(request), comments=None, )
	
	#d = dict( form=PostForm(), user=request.user )
	d = dict( form=myPostForm(), user=request.user )
	d.update(csrf(request))
	
	#print RequestContext(request)
	
	return render_to_response("q_a_post.html", d, context_instance = RequestContext(request))
	

"""
# Show post form with Image
def show_post_form2(request):
	''' Show Post form. '''
	
	post_formset = formset_factory(PostForm)
	image_formset = formset_factory(ImagesForm)
	
	#d = dict( form=PostForm(), user=request.user )
	d = dict( imgform=image_formset(), postform = post_formset(), user=request.user )
	d.update(csrf(request))
	
	#print RequestContext(request)
	
	return render_to_response("q_a_create_post.html", d, context_instance = RequestContext(request))
	

"""

#========


# Add a Question
# DONE
def add_post(request):
	
	if request.method == 'POST':
		p = request.POST
		
		if p.has_key('content') and p["content"]:
			content = p["content"]
		
		if p.has_key('title') and p["title"]:
			title = p["title"]
		
		if p.has_key('tags') and p["tags"]:
			tags = p["tags"]
			
		ip = get_client_ip(request)
		user = request.user
		#~d.update(csrf(request))
		
		# Adding all stuff into DB, so i think we shouldn't use,
		# get_or_create here, but instead, just use create
		#pk = Post.objects.get_or_create( title=title, content=content, user_ip=ip, slug=slug, user_id = user.id)
		pk, cr = Post.objects.get_or_create( title=title, content=content, user_ip=ip, user_id = user.id, tags=tags)
		
		# True condition, 
		# If everything goes fine, 
		# show the primary key For The Moment
		# Actually supposed to redirect to the page where user came from
		#~return HttpResponseRedirect(reverse("q_a.views.view_post_id", args=[pk]))
		return HttpResponseRedirect(reverse("q_a.views.view_post_id", args=[pk.id, pk.slug] ))
		#~return HttpResponse(pk)
	
	#d = {'postform': post_formset, 'imgform': image_formset}
	# if condition False, Else show the form again
	return HttpResponseRedirect(reverse("q_a.views.show_post_form"))
	

# Form for Comment(reply) to an Answer
def show_reply_form(request, pk):
	
	pk = Post.objects.get(pk=pk)
	
	fromUrl = request.GET['from']
	d = dict( form=myPostForm( exclude_list=['title'] ), user=request.user , pk=pk.id, fromUrl = fromUrl)
	
	# d = dict( form=PostForm(), user=request.user )
	
	d.update(csrf(request))
	return render_to_response("q_a_post.html", d, context_instance = RequestContext(request))
	#~return HttpResponse(request.user)
	

# Add Comment(reply) to an Answer
def add_reply(request, pk):
	
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
	# If its not a post, then just redirect to the reply form again
	return HttpResponseRedirect(reverse("q_a.views.show_reply_form"))
	

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
		d = dict( by_user=request.user, status=status )
		
		li = p.vote_set.filter(**d)
		
		# if length(li) > 1, then log it to the logs, as it is a problem, as 1 user can only make 1 vote to a particular Post
		
		# by default 1 user can vote to a post_id only once
		if li:
			obj = li[0]
			obj.vote = vote
			obj = obj.save()
		else:
			d["vote"] = vote
			obj = p.vote_set.create(**d)
		
		cr = None
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
		
		#~print "request.GET['from']"
		#~print request.GET['from']
		
		f =request.GET['from']
		
		
		return HttpResponseRedirect(f)
	else:
		return HttpResponse('Please Login here.')
	

# DONE
#@login_required
def follow(request, pk, follow, typ ):
	"""Follow: 
	Will get the Post id, and +1 or -1 as Follow or Unfollow"""
	
	#~p = Post.objects.get(pk=pk)
	
	follow = int(follow)
	
	foll = None
	foll, cr = Follow.objects.get_or_create( by_user=request.user, fieldTypeId=pk, fieldType=typ )
	
	foll.follow = follow
	foll.save()
	
	fromUrl =request.GET['from']
	
	return HttpResponseRedirect(fromUrl)
	#~d = dict( p = post, follow=foll, fromUrl = fromUrl)
	#~return render_to_response ('q_a_post_id.html', d)
	


#~# Share
#~def share(request, pk):
	#~
	#~# Deactivated for the moment
	#~status = static['vote_field_default_status']
	#~
	#~s = Share.objects.all()
	#~obj, cr = s.get_or_create( post_id=pk, by_user=request.user, status=status)
	#~
	#~cr = 1
	#~# If an object was created
	#~if cr:
		#~pass
	#~# else, if it was not created
	#~else:
		#~pass
	#~
	#~#return HttpResponse(cr)
	#~return HttpResponse(s)
	#~


# pk parameter for post_id, & share parameter, bcoz we thought, we can give +1 to share & then -1 to UnShare
# But, now only, pk parameter for post_id , as share will always happen & User CANNOT UnShare, theres no such thing as UnShare.
#def share(request, pk, share):
def share(request, pk):
	"""#Share: Will get the Post id, and +1 or -1 as share
	No such thing as UnShare, only Share allowed
	"""
	
	#share = int(share)
	# FTM
	share = 1
	
	p = Post.objects.get(pk=pk)
	
	# Deactivated for the moment
	status = static['vote_field_default_status']
	u = static['root_user_id']
	
	# Login required, if we put it in the descriptor, we dont have to use this if condition,
	# using only FTM
	if request.user.id:
		#d = dict( by_user=request.user, vote=vote, status=status )
		#d = dict( by_user=request.user, post=pk, share=share)
		d = dict( by_user=request.user, post=p, share=share)
		
		# by default 1 user can vote to a post_id only once
		#obj, cr = p.share_set.get_or_create(**d)
		obj, cr = Share.objects.get_or_create(**d)
		
		# If an object was created
		#if cr:
			#pass
		# else, if it was not created
		#else:
			#pass
		
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
	
	import settings
	
	#~return HttpResponse( request._cookies )
	#~return HttpResponse( request.session )
	#~return HttpResponse( st )
	return HttpResponse( dir(settings) )
	#~return HttpResponse( r )
	#~return HttpResponse( t )
	

