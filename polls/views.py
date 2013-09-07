# Create your views here.
from django.http import HttpResponse, Http404

from polls.models import *
from django.http import HttpResponse, HttpResponseRedirect
from django.template import Context, loader
from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext

from django.core.urlresolvers import reverse


#~def index(request):
	#~latest_poll_list = Poll.objects.order_by('-pub_date')[:5]
	#~t = loader.get_template("index.html")
	#~c = Context({
		#~"latest_poll_list": latest_poll_list,
	#~})
	#~return HttpResponse(t.render(c))
#~
#~
#~def detail(request, poll_id):
	#~#try:
		#~#p = Poll.objects.get(pk=poll_id)
	#~#except Poll.DoesNotExist:
		#~#raise Http404
	#~
	#~p = get_object_or_404(Poll, pk=poll_id)
	#~
	#~#d = {'poll': p}
	#~d = dict(poll=p)
	#~context_instance=RequestContext(request)
	#~
	#~#return HttpResponse("You're looking at poll %s." % poll_id)
	#~return render_to_response("detail.html", d, context_instance )
#~
#~
#~def results(request, poll_id):
	#~p = get_object_or_404(Poll, pk=poll_id)
	#~
	#~# return HttpResponse("You're looking at the results of poll %s." % poll_id)
	#~return render_to_response("results.html", {'poll': p} )

def vote(request, poll_id):
	p = get_object_or_404(Poll, pk=poll_id)
	
	try:
		selected_choice = p.choice_set.get(pk=request.POST['choice'])
	except (KeyError, Choice.DoesNotExist ):
		# Redisplay the poll voting form.
		d = dict(poll=p, error_message="You didn't select a choice.")
		context_instance = RequestContext(request)
		return render_to_response("detail.html", d, context_instance)
	else:
		selected_choice.votes += 1
		selected_choice.save()
	 # Always return an HttpResponseRedirect after successfully dealing 
	 # with POST data. This prevents data from being posted twice 
	 # if a user hits the Back button
	 
		#return HttpResponseRedirect(reverse("polls.views.results", args=(p.id,)))
		# Passing poll_results as now we are using Django Generic Views(see poll urls.py)
		return HttpResponseRedirect(reverse("polls_results", args=(p.id,)))



