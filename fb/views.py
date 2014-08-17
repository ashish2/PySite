# Create your views here.

from minbase.includes import *
import urllib2
from fb.forms import FBUserProfileForm
from fb.models import FBUserProfile
from django.contrib.auth import authenticate, login


def prepare_url_to_call_graph_api(endpoint, access_token):
	graph_url = 'https://graph.facebook.com'
	url = graph_url+ endpoint+'?access_token='+access_token
	return url

def call_graph_api_get_data(url):
	req = urllib2.Request(url)
	resp = None
	if req:
		resp = urllib2.urlopen(req)
	return resp

def prepare_json_data(req):
	st = req.read()
	di = json.loads(st)
	return di

def create_fb_user(di):
	pass
	fb_id = di.pop('id')
	user, create = FBUserProfile.objects.get_or_create(pk=fb_id)
	
	if create:
		pass
		#create a UserProfile and input details
		#request.POST.get('fb_response[id]')
	else:
		pass
		#do nothing
	

def auth_login_user():
	pass
	# Authenticate & log in the user with his email id, & None as password
	#authenticate(user, response)
	#login(user, None)
	

def pull_user_image():
	url_pic = graph_url+'/me/picture?access_token='+access_token+'&height=200&type=normal&width=200&redirect=false'
	#req_data_me_pic = u.Request(url_pic)
	
	# import urllib
	# urllib.urlretrieve("http://domain.name/folder/media/some-pic.jpg", "save-as-local-file.jpg")


def pull_user_me():
	""" Call `/me` endpoint get data of the user by passing access_token & echo data here,  # which the js function will then show."""
	endpoint = '/me'
	return endpoint

def fb_data(response):
	"""All these will just return their respective json data"""
	
	print 1

	accesstoken = response.POST.get('fb_response[authResponse][accessToken]')
	endpoint = pull_user_me()
	url = prepare_url_to_call_graph_api(endpoint, accesstoken)
	resp = call_graph_api_get_data(url)
	di = prepare_json_data(resp)
	
	print 2

	di['fb_id'] = di.get('id')
	di['accesstoken'] = accesstoken
	di['response'] = str( resp.read() )
	# Settings is_active to True for the moment
	di['is_active'] = True
	

	print di


	# if create happens only then create User
	# otherwise, just set session & redirect 
	# u = form.get_or_create()

	#create fbuser
	user = FBUserProfile.objects.filter(fb_id=di['fb_id'])
	# If not user create a user
	if not user:
		form = FBUserProfileForm(di)

		print "bound", form.is_bound
		print "errors", form.errors
		print "valid", form.is_valid()

		# and not form.errors
		if form.is_bound and form.is_valid():
			#enter fb_id, accesstoken, & then pass the POST variable to see if all fields are filled,
			#& then save, other wise u will hav to manually save each field by doing a save(commit=False)
			user = form.save()
		else:
			print "Some errors while logging in."
	else:
		user = user[0]

	#then, #authenticate #&login #& redirect to '/'
	fb_user = authenticate(email=user.email, password=user.password)

	if fb_user is not None:
		if fb_user.is_active:
			#login(request, fb_user)
			login(response, fb_user)
			return HttpResponseRedirect(reverse("stpros.views.list_all"))
		else:
			print "Not active"
	else:
		print 'fb_user is None'

	return di

