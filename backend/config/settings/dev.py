from .base import *
from decouple import config

DEBUG = True

ALLOWED_HOSTS = ['*']  # during development

# Use SQLite for simple local dev OR PostgreSQL
DATABASES['default'] = {
    'ENGINE': 'django.db.backends.postgresql',
    'NAME': config('POSTGRES_DB', default='deltafleet'),
    'USER': config('POSTGRES_USER', default='deltauser'),
    'PASSWORD': config('POSTGRES_PASSWORD', default='deltapass'),
    'HOST': config('POSTGRES_HOST', default='localhost'),
    'PORT': config('POSTGRES_PORT', default='5432'),
}

# Show detailed error logs in development
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'root': {
        'handlers': ['console'],
        'level': 'DEBUG',
    },
}
