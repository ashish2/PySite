# Create your views here.

from minbase.includes import *
from googleapp.forms import *

def list_all(request):
	try:
		user = Guser.objects.get(user_id=request.user.id)
		listToShow = Attendance.objects.filter(guser=request.user.guser).order_by('-pub_date')
		# listing = RealEstateListing.objects.get(slug_url=slug)
		template = 'ga_some_list.html'
	except Guser.DoesNotExist:
		listToShow = []
		template = 'nothing_here.html'
	if not listToShow:
		listToShow = []
		template = 'nothing_here.html'

	d = dict(somelist = listToShow, )
	return render_to_response(template, d, context_instance=RequestContext(request) )


def add_reply(request, pk):
	pass


def read(request, pk):
	pass


def create(request):
	if request.method == 'POST':
		form = AttendanceForm(request.POST)
		if not form.errors and form.is_valid():
			form.save(request, True)
	
	f = AttendanceForm()
	d = dict( form = f, )
	return render_to_response( 'ga_some_post_form.html', d, context_instance=RequestContext(request) )


def edit(request, pk):

	inst = Attendance.objects.filter(pk=pk)
	if inst:
		inst = inst[0]
	else:
		inst = None
	if request.method == 'POST':
		inst.hours = request.POST.get('hours')
		inst.pub_date = request.POST.get('pub_date')
		inst.save()
	f = AttendanceForm( instance=inst)
	d = dict( form = f, )
	return render_to_response( 'ga_some_post_form.html', d, context_instance=RequestContext(request) )



# def login(request):
	# On gplus login, send data hre,
	# create user if not exists
	# if exists return user & 
	# set request.session.google_id of the GUser
	# & return true
	# & use this function as a decorator as glogin
	# to see other functions(pages, edit pages)
	# most list pages can be accessed without this login

	# Guser.objects.filter(gid=authResponse['gplus_id'])
	# request.session.google_id = authResponse['gplus_id']

	# return HttpResponse("Login")




# def login(response):
# 	print "login"
# 	pass


# ============ FB TYPE FUNCTIONALITY ============

# Create your views here.

from minbase.includes import *
import urllib2
from fb.forms import FBUserProfileForm
from fb.models import FBUserProfile
from django.contrib.auth import authenticate, login

from emailusernames.utils import create_user, create_superuser, get_user
from emailusernames.forms import user_exists


def prepare_url_to_call_graph_api(endpoint, access_token):
	# graph_url = 'https://graph.facebook.com'
	
	graph_url = "https://www.googleapis.com/plus/v1/people"
	# endpoint = endpoint
	# access_token = access_token
	acc_tok = "?access_token="

	url = graph_url + endpoint+ acc_tok + access_token
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
	

def pull_user_image(response, di):
	import urllib
	from urlparse import urlparse
	
	url = di.get('image')['url']
	imgUrl = urlparse(url)
	imageExt = imgUrl.path.split('.')[-1]
	user = response.user
	userEmailNameId_userId_imageExtension = 'uploads/avatar/'+str(user.email.split('@')[0])+str(user.pk)+'.'+str(imageExt)
	image = urllib.urlretrieve(url, userEmailNameId_userId_imageExtension)
	return image[0]


def pull_user_me():
	""" Call `/me` endpoint get data of the user by passing access_token & echo data here,  # which the js function will then show."""
	endpoint = '/me'
	return endpoint

def gp_data(response):
	"""All these will just return their respective json data"""

	di = json.loads(response.POST.get("response"))
	accesstoken = di.get("access_token")
	endpoint = pull_user_me()
	# image = pull_user_image(di)

	url = prepare_url_to_call_graph_api(endpoint, accesstoken)

	resp = call_graph_api_get_data(url)
	di = prepare_json_data(resp)

	di['gid'] = di.get('id')
	di['name'] = ' ' . join ( di.get("name").values() )
	di['gender'] = di.get('gender')
	di['profile_link'] = di.get('url')
	di['accesstoken'] = accesstoken
	di['response'] = str( resp.read() )
	di['designation'] = "NA"
	# Settings is_active to True for the moment
	di['is_active'] = True
	# di['avatar'] = image

	# if create happens only then create User
	# otherwise, just set session & redirect 
	#create fbuser
	email = None
	for k in di.get("emails"):
		if k['type'] == 'account':
			email = k['value']
	password = "!"

	print "email"
	print email

	# if email is empty throw error
	if not email:
		raise Exception("No email present")

	# =========
	# if user has email id like
	# then redirect to Restricted Email Detected Page
	# then If email not '@samhita.org'
	# again Restricted Email Detected page
	# if not a samhita.org email, again redirect to restricted_emails page
	
	# if '@samhita.org' not in email:
	# 	return HttpResponseRedirect("/")

	# restricted_emails = [ 'all@samhita.org', 'mail@samhita.org', 'admin@samhita.org' ]
	# for k in restricted_emails:
	# 	if email in restricted_emails[k]:
	# 		# redirect to restricted_emails page
	# 		return HttpResponseRedirect("/")
	# =========

	# If not user, then create
	if not user_exists(email):
		# Create User		
		create_user(email, password)
	# else:
	# 	# user = User.objects.filter(email=email)
	# 	# user = user[0]
	# 	user = get_user(email)
		
	user = get_user(email)
	response.user = user

	di['avatar'] = pull_user_image(response, di)

	print "user"
	print user

	# Create UserProfile
	user_p, cr = UserProfile.objects.get_or_create(user=user)
	# user_p = UserProfileForm(di, user=user)
	user_p.avatar = di['avatar']
	user_p.save()
	# Create FBUserProfile
	fb_user_p = Guser.objects.filter(user=user, gid=di['gid'])

	# If not user create a user
	if not fb_user_p:
		print "NOT FB"
		form = GuserForm(di)
		print "form"
		print form

		print "errors"
		print form.errors
		fb_user_p = form.save(response, commit=False)
		fb_user_p.user = user

		# and not form.errors
		if form.is_bound and form.is_valid():
			print "isbound isvalid"
			#enter fb_id, accesstoken, & then pass the POST variable to see if all fields are filled,
			#& then save, other wise u will hav to manually save each field by doing a save(commit=False)
			form.save(response, commit=True)

		else:
			print "Some Gplus FOrm invalid error errors while logging in."

	#then, #authenticate #&login #& redirect to '/'
	# fb_user = authenticate(email=user.email, password=user.password)
	fb_user = authenticate(email=user.email, password=password)

	if fb_user is not None:
		if fb_user.is_active:
			print "is active"
			#login(request, fb_user)
			login(response, fb_user)
			# redirect here
			return HttpResponseRedirect(reverse("googleapp.views.list_all"))
		else:
			print "Not active"
	else:
		print 'fb_user is None'

	return di


# Example Response from Google Plus
"""
di = {
	'response': '', 
	u'kind': u'plus#person', 
	u'displayName': u'Ashish Ojha', u'name': u'Ashish Ojha', u'language': u'en', 
	u'isPlusUser': True, 
	u'url': u'https://plus.google.com/+AshishOjha2', 
	u'gender': u'male', 
	u'image': {
		u'url': u'https://lh5.googleusercontent.com/-QoejspCFJ2w/AAAAAAAAAAI/AAAAAAAAAL4/_VFUv5YGAww/photo.jpg?sz=50',
		u'isDefault': False
	}, 
	'is_active': True, 'designation': 'NA', 
	u'emails': [
		{
			u'type': u'account', 
			u'value': u'vickyojha@gmail.com'
		}
	], 
	u'etag': u'"L2Xbn8bDuSErT6QA3PEQiwYKQxM/FGjG2snWnTa5_e-flSJssjCI4MA"', 
	'gid': u'115254646172279132383', 
	u'ageRange': {
		u'min': 21
	}, 
	u'verified': False, 
	u'circledByCount': 13, 
	'accesstoken': u'ya29.fAD_2Sg5wvt-qoVehDo0Ki7zSiH5SsrscLff3t7SMjpm3JuFgZAK5QSZ', 
	u'id': u'115254646172279132383', 
	'profile_link': u'https://plus.google.com/+AshishOjha2', 
	u'objectType': u'person'
}
"""
