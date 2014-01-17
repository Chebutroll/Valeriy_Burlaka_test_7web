import os
# Parse database configuration from $DATABASE_URL
import dj_database_url
from .base import *

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

DEBUG = False

TEMPLATE_DEBUG = False

# Allow all host headers
ALLOWED_HOSTS = ['*']

WSGI_APPLICATION = 'myproject.wsgi.prod.application'

DATABASES['default'] = dj_database_url.config()

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
