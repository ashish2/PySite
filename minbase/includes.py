# Create your views here.


### Settings
from mysite.settings import *
#from django.conf.settings import *

### Views

import os
import sys


#from django.views.decorators.cache import cache_page
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.template import Context, loader
from django.template import RequestContext

from django.shortcuts import get_object_or_404, render_to_response

from django.core.urlresolvers import reverse
from django.core.context_processors import csrf
from django.core.paginator import Paginator, InvalidPage, EmptyPage

from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

from django.contrib import auth

# Settings
from mysite import settings

#General
from q_a.func import *

# Models
from django.db.models import Q
from django.db.models import Sum

from q_a.models.models import *

from stpros.models import *


### Models
from django.contrib.auth.models import User
from accounts.models import UserProfile
from relations.models import *

### Some static values
from q_a.staticvals import static


### For generic functions
from urlparse import urlsplit

### Utils
from django.utils import timezone



### Forms
from django.forms.formsets import formset_factory
from stpros.forms import *
from django.forms import TextInput
from accounts.forms import *

from q_a.forms import *

### Formatting
from django.utils.translation import ugettext_lazy as _
#_G=_

import json
from simplejson import loads

### Url
import urllib2



### Bbcode
