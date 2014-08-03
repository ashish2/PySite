from fb.models import FBUserProfile
from django.contrib.auth.backends import ModelBackend

class EmailAuthBackend(ModelBackend):

	"""Allow users to log in with their email address"""

	def authenticate(self, email=None, password=None, **kwargs):
		# Some authenticators expect to authenticate by 'username'
		if email is None:
			#email = kwargs.get('username')
			email = kwargs.get('email')
		try:
			user = self.get_user(email)
			if user.check_password(password):
				user.backend = "%s.%s" % (self.__module__, self.__class__.__name__)
				return user
		except FBUserProfile.DoesNotExist:
			return None

	#def get_user(self, user_id):
		#try:
			#return User.objects.get(pk=user_id)
		#except User.DoesNotExist:
			#return None
	
	def get_user(self, email, queryset=None):
		"""
		Return the user with given email address.
		Note that email address matches are case-insensitive.
		"""
		
		if queryset is None:
			queryset = FBUserProfile.objects
		
		# Hack, as this file was passing `user_id` to this function
		#/opt/lampp/htdocs/ash3_opt_www/www2/python/venv/venv1_4/lib/python2.7/site-packages/django/contrib/auth/__init__.py in get_user
		#user = backend.get_user(user_id) or AnonymousUser()
		if isinstance(email, long) or isinstance(email, int):
			email = queryset.get(pk = email).email
			
		#return queryset.get(username=_email_to_username(email))
		return queryset.get(email= email)
