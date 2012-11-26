import sys, os

sys.path.insert(0, '/home/lurkin4life/.virtualenv/csce4350/lib/python2.5/site-packages')
sys.path.append(os.getcwd())

os.environ['DJANGO_SETTINGS_MODULE'] = "settings"

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()