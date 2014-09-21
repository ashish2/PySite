# Django settings for mysite project.

# ADDED
# Imports
import os
import sys

# Not Working
# Appending a few directories in environment var PYTHONPATH, 
# as we are now in virtualenv & these modules aren't installed in virtualenv.
#sys.path.append('/usr/local/lib/python2.7/dist-packages')
#print sys.path

# importing some more settings
#import extra_settings
from extra_settings import *

# ADDED-

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS

DATABASES = {
    #'default': {
        #'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        #'NAME': 'mysite',                      # Or path to database file if using sqlite3.
        #'USER': 'root',                      # Not used with sqlite3.
        #'PASSWORD': 'pass',                  # Not used with sqlite3.
        #'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        #'PORT': '3308',                      # Set to empty string for default. Not used with sqlite3.
    #}
    
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        #'NAME': 'mysite',                      # Or path to database file if using sqlite3.
        #~'NAME': 'mysite_1',                      # Or path to database file if using sqlite3.
        'NAME': 'mysite_2',                      # Or path to database file if using sqlite3.
        #'USER': 'root',                      # Not used with sqlite3.
        'USER': 'postgres',                      # Not used with sqlite3.
        'PASSWORD': 'pass',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '5432',                      # Set to empty string for default. Not used with sqlite3.
    }
    
}

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'America/Chicago'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = '/opt/lampp/htdocs/ash3_opt_www/www2/python/venv/venv1_4/pysite_1_4/uploads/'

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = 'http://localhost:8000/media/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
#STATIC_ROOT = ''
STATIC_ROOT = 'static_root'

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/static/'

# ADDED
current_dir = os.path.dirname( __file__ )
# ADDED-

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    
    # ADDED
    current_dir,
    # ADDED-
)




# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    #'django.contrib.staticfiles.finders.DefaultStorageFinder',
    
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = '95)3_!eay1@!1bh+v_6!fxd+e*e0)a@7i+o=*s4tjr_5#&amp;#tb7'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
    
    
    # Added
    
    #~'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.middleware.cache.UpdateCacheMiddleware',
    #~'django.middleware.common.CommonMiddleware',
    'django.middleware.cache.FetchFromCacheMiddleware',
    
    # Added-
    
    
)

ROOT_URLCONF = 'mysite.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'mysite.wsgi.application'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    "/var/www/projects/mysite/templates/django",
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    # Bootstrapped Admin
    #'django_admin_bootstrapped',
    
    # Uncomment the next line to enable the admin:
    'django.contrib.admin',
    
    # Uncomment the next line to enable admin documentation:
    # 'django.contrib.admindocs',
    
    # Added
    # Haystack Search
    #'haystack',
    #'six',
    
    'async',
    
    #minbase
    'minbase',
        
    # Tagging
    'tagging',

    # Social
    #'social',
    'fb',
    
    # BBcode
    #'precise_bbcode',
    #'content_bbcode',
    'bbcode',
        
    # Search, Solr
    'pysolr',
    
    # south
    'south',
    
    # Accounts
    'accounts',
    
    #'polls',
    #'qna',
    'q_a',
    
    # Email as Username
    'emailusernames',
    
    # users
    'users',
    
    # rest framework
    # 'rest_framework',
    # 'tastypie',
    
    # following_followers
    'following_followers',
    
    # stpros
    'stpros',
    
    'relations',
    
    # Added-
    
)


# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

# ADDED

AUTHENTICATION_BACKENDS = (
	'emailusernames.backends.EmailAuthBackend',
	# Uncomment the following to make Django tests pass:
	# 'django.contrib.auth.backends.ModelBackend',
	
)

TEMPLATE_CONTEXT_PROCESSORS = (
    #"django.core.context_processors.auth",
    "django.contrib.auth.context_processors.auth",
    
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.request",
    
    # Adding static context processor
    "django.core.context_processors.static",
    
    
)


CACHES = {
	'default': {
		# Memcache
		#'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
		# Memcache
		#'BACKEND': 'django.core.cache.backends.memcached.PyLibMCCache',
		
		# Local Memory Cache
		'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
		
		# For Memcached
		#'LOCATION': '127.0.0.1:11211',
		
		# For LocMem
		'LOCATION': 'unique-snowflake', # Just a name for the cache
	}
}

#CACHE_BACKEND = 'memcached://127.0.0.1:11211/'
CACHE_BACKEND = 'locmem:///var/django/caches/'

# Time to cache
CACHE_MIDDLEWARE_SECONDS = 600

# String To prevent cross site collision
# Keeping it empty FTM
CACHE_MIDDLEWARE_KEY_PREFIX = ''

# True/False , True for all Anonymous request that are made by not logged in user
CACHE_MIDDLEWARE_ANONYMOUS_ONLY = True


# Appending This Dir into the sys.path for python
sys.path.append(os.path.dirname(__file__))

# models.models.UserProfile
AUTH_PROFILE_MODULE = "accounts.UserProfile"

# Login
LOGIN_URL = '/accounts/login/'


# importing some more settings at the End
from extra_heroku_end_settings import *

# ADDED-
