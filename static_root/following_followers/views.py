# Create your views here.


def show_followers(pk):
	"""Show who are the Followers of this User, Select from Followers table"""
	followers = Followers.objects.filter(pk=pk)
	pass

def show_following(pk):
	"""Show who this user is Following, select from Following table"""
	following = Following.objects.filter(pk=pk)
	pass


def add_followers(toThatUid, addMyUid):
	"""I will Follow HIM, add myUid to thatUid"""
	# Finally redirect to the fromUrl
	#Followers.object.get_or_create(user = toThatUid, followers=response.user.id)
	pass

def remove_followers(fromThatUid, removeMyUid):
	"""I will UnFollow HIM, removeMyUid - fromThatUid"""
	# Finally redirect to the fromUrl
	#Followers.object.delete(user = fromThatUid, following=response.user.id)
	pass
	
