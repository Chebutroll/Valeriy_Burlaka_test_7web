from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = []

# Application definition
WSGI_APPLICATION = 'myproject.wsgi.dev.application'

DATABASES['default'] = {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, '7webtest.db'),
}

INSTALLED_APPS += ('django_coverage',)

COVERAGE_REPORT_HTML_OUTPUT_DIR = os.path.join(BASE_DIR, 'coverage')


