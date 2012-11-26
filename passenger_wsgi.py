import sys, os

INTERP = os.path.join(os.environ['HOME'], '.virtualenvs', 'project_name', 'bin', 'python')
if sys.executable != INTERP:
    os.execl(INTERP, INTERP, *sys.argv)

sys.path.insert(0, '/home/lurkin4life/.virtualenv/csce4350/lib/python2.5/site-packages')
sys.path.append(os.getcwd())

os.environ['DJANGO_SETTINGS_MODULE'] = "settings"

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()