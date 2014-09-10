# Create your views here.

from minbase.includes import *
import urllib2
from fb.forms import FBUserProfileForm
from fb.models import FBUserProfile
from django.contrib.auth import authenticate, login

from emailusernames.utils import create_user, create_superuser, get_user
from emailusernames.forms import user_exists


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
	email = di.pop("email")
	# user, create = FBUserProfile.objects.get_or_create(pk=fb_id)
	# user, create = User.objects.get_or_create(email=email)

	password = None

	if not user_exists(email):
		create_user(email, password)

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
	
	accesstoken = response.POST.get('response[authResponse][accessToken]')
	endpoint = pull_user_me()

	url = prepare_url_to_call_graph_api(endpoint, accesstoken)
	resp = call_graph_api_get_data(url)
	di = prepare_json_data(resp)
	

	di['fb_id'] = di.get('id')
	di['accesstoken'] = accesstoken
	di['response'] = str( resp.read() )
	# Settings is_active to True for the moment
	di['is_active'] = True
	
	# if create happens only then create User
	# otherwise, just set session & redirect 
	# u = form.get_or_create()

	#create fbuser
	email = di.pop("email")
	password = "!"

	# If not user, then create
	if not user_exists(email):
		# Create User		
		create_user(email, password)
		user = get_user(email)

		# Create UserProfile
		user_p, cr = UserProfile.objects.get_or_create(user=user)
		# Create FBUserProfile
		fb_user_p = FBUserProfile.objects.filter(user=user, fb_id=di['fb_id'])

		# If not user create a user
		if not fb_user_p:
			form = FBUserProfileForm(di)

			fb_user_p = form.save(commit=False)
			fb_user_p.user = user

			# and not form.errors
			if form.is_bound and form.is_valid():
				#enter fb_id, accesstoken, & then pass the POST variable to see if all fields are filled,
				#& then save, other wise u will hav to manually save each field by doing a save(commit=False)
				form.save(commit=True)

			else:
				print "Some FB Form invalid error errors while logging in."
	else:
		# user = User.objects.filter(email=email)
		# user = user[0]
		user = get_user(email)
		

	#then, #authenticate #&login #& redirect to '/'
	# fb_user = authenticate(email=user.email, password=user.password)
	fb_user = authenticate(email=user.email, password=password)

	if fb_user is not None:
		if fb_user.is_active:
			#login(request, fb_user)
			login(response, fb_user)
			# redirect here
			return HttpResponseRedirect(reverse("stpros.views.list_all"))
		else:
			print "Not active"
	else:
		print 'fb_user is None'

	return di

