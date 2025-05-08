from .base import *
from decouple import config

DEBUG = True

ALLOWED_HOSTS = ['*']  # during development

# Use SQLite for simple local dev OR PostgreSQL
DATABASES['default'] = {
    'ENGINE': 'django.db.backends.postgresql',
    'NAME': config('POSTGRES_DB'),
    'USER': config('POSTGRES_USER'),
    'PASSWORD': config('POSTGRES_PASSWORD'),
    'HOST': config('POSTGRES_HOST'),
    'PORT': config('POSTGRES_PORT'),
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
