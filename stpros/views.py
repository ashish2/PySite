# Create your views here.

from q_a.staticvals import *
from minbase.includes import *

def hi_from_fb(request):
	
	print "GET"
	print request.GET
	print "POST"
	print request.POST
	
	return HttpResponse("Hi from FB")


def list_all(request):
	
	listToShow = PathToSolution.objects.filter(parent_id=None).order_by("-date")
	paginator = Paginator(listToShow, 5)
	try:
		page = int(request.GET.get("page", "1"))
	except ValueError:
		page = 1
		
	try:
		listToShow = paginator.page(page)
	except (InvalidPage, EmptyPage):
		listToShow = paginator.page(paginator.num_pages)
	
	for li in listToShow.object_list:
		e = None
		e = li.vote_set.filter( pts_id=li.id, user=request.user.id )
		# this means he has voted something 			# 0, which means he hasn't voted
		li.has_voted = e[0].vote if e else 0
		vote_count = li.vote_set.aggregate(Sum('vote'))['vote__sum']
		li.vote_count = vote_count if vote_count else 0
	
	fromUrl = request.get_full_path()
	d = dict(somelist = listToShow, fromUrl = fromUrl )
	
	return render_to_response( 'some_list.html', d, context_instance=RequestContext(request) )




@login_required
def create(request):
	
	if request.method == 'POST':
		form = PathToSolutionForm(request.POST, exclude=('slug', 'parent_id', ))
		if form.is_bound:
			if form.is_valid():
				clean_data = form.cleaned_data
				form.instance.problem = form.cleaned_data.get('problem')
				form.instance.answer = form.cleaned_data.get('answer')
				form.save(request)
				#return render_to_response('stpros_list.html', d, context_instance=RequestContext(request) )
			else:
				"Form Invalid"
				form.errors
				pass
		else:
			"No data received in form"
			pass
	else:
		"Some problem occurred while submitting the form"
		pass
	
	func_name = sys._getframe().f_code.co_name
	form_action = reverse('stpros.views.'+func_name )
	d = dict(form=PathToSolutionForm(exclude=('slug', 'parent_id', )), form_action = form_action, )
	
	#fromUrl = request.GET.get('fromUrl')
	#if fromUrl:
		#return HttpResponseRedirect(fromUrl)
	
	#return render_to_response( 'stpros_form.html', d, context_instance=RequestContext(request) )
	return render_to_response( 'some_post_form.html', d, context_instance=RequestContext(request) )
	

# Form for Comment(reply) to an Answer
def add_reply(request, pk):
	
	fromUrl = request.GET.get('from')
	
	if request.method == 'POST':
		form = PathToSolutionForm(request.POST, exclude=('problem', 'slug', 'parent_id', ) )
		
		if form.is_bound:
			if form.is_valid():
				clean_data = form.cleaned_data
				#form = form.save(request, commit=False)
				PTS_instance = PathToSolution.objects.get(pk=pk)
				form.instance.parent_id = PTS_instance
				form.instance.answer = form.cleaned_data.get('answer')
				form.save(request)
				if fromUrl:
					return HttpResponseRedirect(fromUrl)
			else:
				"Form Invalid"
				form.errors
				pass
		else:
			"No data received in form"
			pass
	else:
		"Some problem occurred while submitting the form"
		pass
	
	
	#d = dict(form=PathToSolutionForm,)
	form=PathToSolutionForm( exclude=( 'problem' , 'slug', 'parent_id' ) )
	func_name = sys._getframe().f_code.co_name
	form_action = reverse('stpros.views.'+func_name, args=[pk])
	
	d = dict( form=form, user=request.user, pk=pk, fromUrl = fromUrl, form_action = form_action, )
	d.update(csrf(request))
	
	return render_to_response( 'some_post_form.html', d, context_instance=RequestContext(request) )


def read(request, pk):
#def view_post_id(request, pk, slug):
	post = PathToSolution.objects.get(id=pk)
	replies = PathToSolution.objects.filter(parent_id=post).order_by("-date")
	fromUrl = request.get_full_path()
	
	for li in replies:
		e = None
		e = li.vote_set.filter( pts_id=li.id, user=request.user.id )
		# this means he has voted something 			# 0, which means he hasn't voted
		li.has_voted = e[0].vote if e else 0
		vote_count = li.vote_set.aggregate(Sum('vote'))['vote__sum']
		li.vote_count = vote_count if vote_count else 0
	
	
	d = dict( some_id = post, replies=replies, fromUrl=fromUrl)
	return render_to_response('read_some_particular_id.html', d, context_instance = RequestContext(request) )
	


@login_required
def vote(request, pk, vote):
	"""VOTES: 
	Will get the PTS id, and +1 or -1 as vote"""
	
	vote = int(vote)
	p = PathToSolution.objects.get(pk=pk)
	
	# Deactivated for the moment
	status = static['vote_field_default_status']
	u = static['root_user_id']
	
	# Login required, if we put it in the descriptor, we dont have to use this if condition, 	# using only FTM
	if request.user.id:
		d = dict( user=request.user, is_active=status )
		
		li = p.vote_set.filter(**d)
		
		# if length(li) > 1, then log it to the logs, as it is a problem, as 1 user can only make 1 vote to a particular PTS
		
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
		
		f =request.GET['from']
		
		return HttpResponseRedirect(f)
	else:
		return HttpResponse('Please Login here.')
	

