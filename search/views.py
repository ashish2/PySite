# Create your views here.

from minbase.includes import *


def main(request):
	print "request.GET"
	print request.GET.get("q")

	return HttpResponse("So, here we are, starting probably 1 of the most legendary modules that we will ever write and build, called: `The Search.`")



