
from q_a.includes import *

from tastypie.authorization import *

from tastypie.resources import ModelResource
from tastypie.authentication import *

from django.db import models

from tastypie.models import create_api_key

from tastypie import fields


models.signals.post_save.connect(create_api_key, sender=User)


class UserResource(ModelResource):
	class Meta:
		queryset = User.objects.all()
		resource_name = 'user'
		#~resource_name = 'auth/user'
		exclude = ['email', 'password', 'is_active', 'is_staff', 'is_superuser']
		#~allowed_methods = ['get']
		# Authentication
		authentication = ApiKeyAuthentication()
		
	

class PostResource(ModelResource):
	user = fields.ForeignKey(UserResource, 'user')
	
	class Meta:
		queryset = Post.objects.all()
		resource_name = 'post'
		authorization = Authorization()
	






