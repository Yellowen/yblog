import os
import sys

DEBUG = True
TEMPLATE_DEBUG = DEBUG

DEPLOYMENT = False

ADMINS = (
    ('Sameer Rahmani', 'lxsameer@yellowen.com'),
)

MANAGERS = ADMINS

ROOT = os.path.dirname(__file__)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(ROOT, '../db/db.sqlite'),
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}

if DEPLOYMENT:
    if os.path.exists(os.path.join(ROOT, "conf/pgsecret")):
        pgsec = file(os.path.join(ROOT, "conf/pgsecret")).read().strip()
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'yblog',
            'USER': 'ublog',
            'PASSWORD': pgsec,
            'HOST': '',
            'PORT': '',
            }
        }

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'America/Chicago'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

_ = lambda s: s

LANGUAGES = [
    ["fa", _("Persian")],
    ["en", _("English")],
]


SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = False

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = os.path.join(ROOT, "../media/statics/")

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = '/statics/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = os.path.join(ROOT, "../statics")

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/statics/'

#ADMIN_MEDIA_PREFIX = '/statics/admin/'

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'q_#ilqm_7y%5zjsbjrcg%r66#7sgu@a^!2_afapz%w-2yy(gze'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'daarmaan.client.middlewares.DaarmaanAuthMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'ultra_blog.middlewares.BlogMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'vanda.core.middlewares.crossdomain.XsSharing',
)

ROOT_URLCONF = 'yblog.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'servers.wsgi.application'

TEMPLATE_DIRS = (
    os.path.join(ROOT, '../media/templates'),
    os.path.join(ROOT, '../media/blog_templates'),

)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.admin',
    'django.contrib.comments',
    #'django.contrib.markup',
    'vanda.core',
    'daarmaan.client',
    'vanda.apps.page',
    'haystack',
    'tagging',
    'robots',
    'ultra_blog',
    #'vanda.apps.dtable',
    'notify',
    'captcha',
    'tastypie',
)

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
            }
        },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'stream': sys.stdout,
            },
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
            }
        },
    'loggers': {
        ## 'django': {
        ##     'handlers': ['console', ],
        ##     'level': 'ERROR',
        ##     'propagate': True,
        ##     },
        'django.request': {
            'handlers': ['mail_admins', 'console'],
            'level': 'ERROR',
            'propagate': True,
            },
        'django.db.backends': {
            'level': 'DEBUG',
            'handers': ['console'],
            },
        }
}

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.request",
    "django.contrib.messages.context_processors.messages",
    #"daarmaan.client.context_processors.urls",
    "utils.projectinfo.info",
    )


CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        'LOCATION': os.path.join(ROOT, '../.cache'),
    }
}

DOMAIN = "yellowers.com"

# Email settings ---------------------------
try:
    from conf import smtp_settings

    EMAIL_HOST = smtp_settings.EMAIL_HOST
    EMAIL_PORT = smtp_settings.EMAIL_PORT
    EMAIL_HOST_USER = smtp_settings.EMAIL_HOST_USER
    EMAIL_HOST_PASSWORD = smtp_settings.EMAIL_HOST_PASSWORD
    EMAIL_USE_TLS = smtp_settings.EMAIL_USE_TLS
    EMAIL = smtp_settings.EMAIL

except ImportError:
    pass


try:
    from conf import recaptcha

    RECAPTCHA_PRIVATE_KEY = recaptcha.PRIV_KEY
    RECAPTCHA_PUBLIC_KEY = recaptcha.PUB_KEY

except ImportError:

    pass


WEBSOCKET_PORT = "9001"
UNIX_SOCKET = "/tmp/websucks.sock"

TITLE = "Yellowen Blog"
VERSION = "3.0.0-b1"
VANDA_VERSION = "2.4.0"

# Setting up search ENGINE
HAYSTACK_SEARCH_ENGINE = 'whoosh'
HAYSTACK_SITECONF = 'conf.search_config'
HAYSTACK_WHOOSH_PATH = os.path.join(ROOT, '.search_index')

# Configuring SSO through Daarmaan service
DAARMAAN_SERVER = "http://daarmaan.yellowen.com:9000"
DAARMAAN_LOGIN = "%s/authenticate/" % DAARMAAN_SERVER
DAARMAAN_LOGOUT = "%s/logout/" % DAARMAAN_SERVER
DAARMAAN_DASHBOARD = "%s/my/" % DAARMAAN_SERVER

SERVICE_NAME = "yellowers.com"
SERVICE_KEY = "123456"

AUTHENTICATION_BACKENDS = (
    'daarmaan.client.backends.DaarmaanBackend',
)

#LOGIN_REDIRECT_URL = "/"
LOGIN_URL = DAARMAAN_SERVER
LOGOUT_URL = "%s/logout" % DAARMAAN_SERVER

GLOBAL_DOMAINS = [
    "www.yellowers.com",
    "yellowers.com",
    "localhost:8000",
    ]


DAARMAAN_EXCLUDE_URLS = [
    r"^/api/",
    ]
