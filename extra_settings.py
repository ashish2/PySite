# Appending a few directories in environment var PYTHONPATH, 
# as we are now in virtualenv & these modules aren't installed in virtualenv.
# Not happening
sys.path.append('/usr/local/lib/python2.7/dist-packages')

# Do this instead, in command line
export PYTHONPATH=$PYTHONPATH:
	"/usr/local/lib/python2.7/dist-packages":
	"/usr/lib/python2.7/dist-packages":
	"/usr/lib/pymodules/python2.7":
	"/opt/lampp/htdocs/ash3_opt_www/www2/python/venv/venv2/lib/python2.7/site-packages":
	"/opt/lampp/htdocs/ash3_opt_www/www2/python/venv/venv1_4/local/lib/python2.7/site-packages":
	"/opt/lampp/htdocs/ash3_opt_www/www2/python/venv/venv1_4/lib/python2.7/site-packages"
	


# Haystack Settings
HAYSTACK_CONNECTIONS = {
	'default': {
		'ENGINE': 'haystack.backends.solr_backend.SolrEngine',
		'URL': 'http://127.0.0.1:8983/solr',
		# ...or for multicore...
		# 'URL': 'http://127.0.0.1:8983/solr/mysite',
	},
}
# Haystack Settings-

