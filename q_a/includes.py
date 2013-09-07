
# Views
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.template import Context, loader
from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.core.context_processors import csrf

#from django.views.decorators.cache import cache_page


from q_a.models import *
from q_a.forms import *
from q_a.func import *


import os
from django.core.paginator import Paginator, InvalidPage, EmptyPage

# Some static values
from q_a.staticvals import static
from django.contrib.auth.models import User




# For generic functions
from urlparse import urlsplit


#Models




