
### Views

import os

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

from django.db.models import Q

from q_a.models.models import *
from q_a.forms import *
from q_a.func import *

### Some static values
from q_a.staticvals import static
from django.contrib.auth.models import User


### For generic functions
from urlparse import urlsplit



### Models



