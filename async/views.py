# Create your views here.
from minbase.includes import *

from fb.views import *


# Whereas, it is supposed to be an
# HttpResponse 200 or something else 
# should be decided here.
def main(request):
	
	funcs = { 
		"fb_data": fb_data,
	}
	
	if request.method == "POST":
		return HttpResponse( funcs[request.POST.get('func_to_run')](request) )
		
	return HttpResponse("Nothing To Show here at the moment")


#accessToken=CAAG6DSHRbK0BALWIz6RcAZCN3oNoqkZBs0dXR3MPKZB8X77dZCj3k3efvPQ1zuMpM5idVQtS2r1JsFN9TwDi4yQSGCGU3P2sGRXuPGRdLXjS9b4l6eLvSsiFYFAeYeUruIF6rKUaq1lmaOw0I3VDBgUN44TapKNnZCL45eR2cOXVq4TAA6bCGW13WsNbNRKJZAoBvE0SJCNLF6aSchj6rftlApRcZAzEHAZD
