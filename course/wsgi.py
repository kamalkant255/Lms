"""
WSGI config for course project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

import os
from dj_static import Cling
from django.core.wsgi import get_wsgi_application

from whitenoise import WhiteNoise

from course import MyWSGIApp


application = MyWSGIApp()
application = WhiteNoise(application, root='/path/to/static/files')
application.add_files('/path/to/more/static/files', prefix='more-files/')


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'course.settings')

#application =Cling(get_wsgi_application())
