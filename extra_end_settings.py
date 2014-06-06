# Settings at the End

### Settings for Heroku
import dj_database_url
DATABASES['default'] = dj_database_url.config()

# honor the 'x_forwarded_proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Allow all hosts headers
ALLOW_HOST = ['*']

# Static asset configuration
import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
#STATIC_ROOT = 'staticfiles'
STATIC_ROOT = ''
STATIC_URL = '/static/'

current_dir = os.path.dirname( __file__ )

STATICFILES_DIRS = (
	#os.path.join(BASE_DIR, 'static'),
	current_dir
)

