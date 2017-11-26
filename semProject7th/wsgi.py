"""
WSGI config for semProject7th project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/
"""

import os
import sys   #newly added

path = '/home/pythonanywhere/projectname'  #newly added
if path not in sys.path:   #newly added
	sys.path.append(path)   #newly added

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "semProject7th.settings")

from django.contrib.staticfiles.handlers import StaticFilesHandler #newly added
application = StaticFilesHandler(get_wsgi_application())  #partially newly added
