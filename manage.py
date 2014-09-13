#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    
    # For Dev
    # ORI for Dev
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
    # Added for Dev
    #os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")
    
    # For Heroku
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "heroku_settings")
    

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
