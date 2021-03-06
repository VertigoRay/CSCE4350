# Django settings for vertigion project.

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = ()

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'com_worleybox_csce4350',                      # Or path to database file if using sqlite3.
        'USER': 'worley_csce4350',                      # Not used with sqlite3.
        'PASSWORD': 'BFHrhbkU6u84m7Amsnpm46pBTvERCfk',                  # Not used with sqlite3.
        'HOST': 'mysql.vertigion.com',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}
# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
# TIME_ZONE = 'America/Chicago'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
# LANGUAGE_CODE = 'en-us'

# SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
# USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale
# USE_L10N = True

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
# MEDIA_ROOT = '/home/vertigion/com.v3pu.media/'

# Mail is sent using the SMTP host and port specified in the EMAIL_HOST and EMAIL_PORT settings. 
# The EMAIL_HOST_USER and EMAIL_HOST_PASSWORD settings, if set, are used to authenticate to the 
# SMTP server, and the EMAIL_USE_TLS setting controls whether a secure connection is used.
# EMAIL_HOST = 'a1.balanced.homie.mail.dreamhost.com'
# EMAIL_PORT = 587
# EMAIL_HOST_USER = 'basura@80.vertigion.com'
# EMAIL_HOST_PASSWORD = 'Tr@$hC@n!'
# EMAIL_USE_TLS = True

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
# MEDIA_URL = 'http://media.v3pu.com/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
# STATIC_ROOT = '/mnt/ras0196/Documents/CSCE4350/com.worleybox.csce4350.genizah/'

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
# STATIC_URL = 'http://media.v3pu.com/'

# Make this unique, and don't share it with anybody.
# SECRET_KEY = 'suy#sm5kd3%$zv6k9d=9(z1z8q0fx##50eyg6z77wt4(zswfpr'

# List of callables that know how to import templates from various sources.
# TEMPLATE_LOADERS = (
#     'django.template.loaders.filesystem.Loader',
#     'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
# )

# MIDDLEWARE_CLASSES = (
#     'django.middleware.common.CommonMiddleware',
#     'django.contrib.sessions.middleware.SessionMiddleware',
#     'django.middleware.csrf.CsrfViewMiddleware',
#     'django.contrib.auth.middleware.AuthenticationMiddleware',
#     'django.contrib.messages.middleware.MessageMiddleware',
# )

# ROOT_URLCONF = 'urls'

# TEMPLATE_DIRS = (
#     Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
#     Always use forward slashes, even on Windows.
#     Don't forget to use absolute paths, not relative paths.
# 	'%s/templates' % os.getcwd(),
# )

# INSTALLED_APPS = (
#     'django.contrib.auth',
#     'django.contrib.contenttypes',
#     'django.contrib.sessions',
#     'django.contrib.sites',
#     'django.contrib.messages',
#     # Uncomment the next line to enable the admin:
#     'django.contrib.admin',
# 	'v3pu',
# )