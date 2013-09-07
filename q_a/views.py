# Create your views here.

# Only 1 import here, which is the include file, 
# all the other modules are imported in includes.py
from q_a.includes import *

#@cache_page(60 * 10)
def view_all_post(request):
	posts = Post.objects.all().order_by("-date")
	paginator = Paginator(posts, 5)
	
	try:
		page = int(request.GET.get("page", "1"))
	except ValueError:
		page = 1
	
	try:
		posts = paginator.page(page)
	except (InvalidPage, EmptyPage):
		posts = paginator.page(paginator.num_pages)
	
	fromUrl = request.get_full_path()
	
	return render_to_response('q_a_list.html', dict( posts=posts, fromUrl=fromUrl ) )
	

def view_post_id(request, pk):
	
	return HttpResponse('Post id')


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
		
	#~return HttpResponseRedirect(reverse("q_a.views.view_post_id", args=[pk]))
		return HttpResponse(pk)
		
	return HttpResponseRedirect(reverse("q_a.views.show_post_form"))
	


def show_comment_form(request, pk):
	
	pk = Post.objects.get(pk=pk)
	d = dict( form=myPostForm( exclude_list=['title'] ), user=request.user , pk=pk.id)
	
	# d = dict( form=PostForm(), user=request.user )
	
	d.update(csrf(request))
	return render_to_response("q_a_post.html", d)
	#return HttpResponse(d)
	

def add_comment(request, pk):
	
	if request.POST:
		p = request.POST
		
		if p.has_key('content') and p["content"]:
			content = p["content"]
		
		po = Post.objects.get(pk=pk)
		
		ip = get_client_ip(request)
		user = request.user
		#~d.update(csrf(request))
		
		pk = Post.objects.get_or_create( title=po.title, content=content, user_ip=ip, user_id = user.id, parent_id=po)
		
	#~return HttpResponseRedirect(reverse("q_a.views.view_post_id", args=[pk]))
		return HttpResponse(pk)
		
	return HttpResponseRedirect(reverse("q_a.views.show_comment_form"))
	

# VOTES
# Will get the Post id, and +1 or -1 as vote
def vote(request, pk, vote):
	vote = int(vote)
	
	p = Post.objects.get(pk=pk)
	
	# Deactivated for the moment
	status = static['vote_field_default_status']
	
	u = static['root_user_id']
	#v = p.vote_set.create(by_user=request.user, vote=vote, status=status)
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
	

def random(request):
	st = ''
	for e in  request.__dict__:
		st += str(e) + '<br />'
	
	st += '<br />'
	
	#~for e in request.items():
		#~st += str(e) + '<br />'
	
	# type(request)
	
	
	
	return HttpResponse( request._cookies )
	#~return HttpResponse( st )
	

