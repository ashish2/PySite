import os
from settings import DATABASES

# Settings at the End

### Settings for Heroku
import dj_database_url
#DATABASES['default'] = dj_database_url.config()
#DATABASES['default'] = dj_database_url.config()
DATABASES['default'] = dj_database_url.config(default=os.environ.get('DATABASE_URL'))

print "DATABASES"
print DATABASES


# honor the 'x_forwarded_proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Allow all hosts headers
ALLOW_HOST = ['*']

# Static asset configuration
import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
#STATIC_ROOT = 'staticfiles'
STATIC_ROOT = 'static'
STATIC_URL = '/static/'

current_dir = os.path.dirname( __file__ )

STATICFILES_DIRS = (
	os.path.join(BASE_DIR, 'static'),
	current_dir,
)

#postgres://hpyhbrdkfhuyde:w5JW3maVZAiKBdWbuYQG_dqM2_@ec2-54-204-2-255.compute-1.amazonaws.com:5432/d7kett2c1qs016
