import os, sys
from config.settings.base import BASE_DIR

sys.path.insert(0, os.path.join(BASE_DIR, 'apps'))

settings_mode = os.getenv("DJANGO_SETTINGS_MODULE", "config.settings.dev")
exec(f"from {settings_mode} import *")
