# settings/dev.py
# python manage.py runserver --settings=app_config.settings.dev

from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [
    'app1.ccc.tw.local',
    '192.168.66.10',
    'localhost',
    '127.0.0.1',
]

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

#  DATABASES = {
#      'default': {
#          'ENGINE': 'django.db.backends.sqlite3',
#          'NAME': BASE_DIR / 'db.sqlite3',
#      }
#  }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'app1_db',
        'USER': 'app1_user',
        'PASSWORD': 'Passw0rd',
        'HOST': '127.0.0.1',
        'PORT': '5432',
        'OPTIONS': {
            'sslmode': 'require'
        }
    }
}
