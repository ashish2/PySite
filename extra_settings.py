# Appending a few directories in environment var PYTHONPATH, 
# as we are now in virtualenv & these modules aren't installed in virtualenv.
# Not happening
sys.path.append('/usr/local/lib/python2.7/dist-packages')

# Do this instead, in command line
export PYTHONPATH=$PYTHONPATH:
	"/usr/local/lib/python2.7/dist-packages":
	"/opt/lampp/htdocs/ash3_opt_www/www2/python/venv/venv2/lib/python2.7/site-packages":
	


