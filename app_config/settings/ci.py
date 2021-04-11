# settings/dev.py
# python manage.py runserver --settings=app_config.settings.dev
import environ
from .base import *

root = environ.Path(__file__) - 3
env = environ.Env()

# reading .env file
environ.Env.read_env()

SITE_ROOT = root()

# SECURITY WARNING: don't run with debug turned on in production!

# False if not in os.environ
DEBUG = env.bool('DEBUG', default=False)

# Raises django's ImproperlyConfigured exception if SECRET_KEY not in os.environ
SECRET_KEY = env.str('SECRET_KEY')

ALLOWED_HOSTS = [
    'app1.ccc.tw.local',
    '192.168.66.10',
    'localhost',
    '127.0.0.1',
]

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': env.str('DB_NAME'),
        'USER': env.str('DB_USER'),
        'PASSWORD': env.str('DB_PASS'),
        'HOST': env.str('DB_HOST'),
        'PORT': env.str('DB_PORT'),
        'OPTIONS': {
            'sslmode': 'require'
        }
    }
}

#  DATABASES = {
#      'default': {
#          'ENGINE': 'django.db.backends.sqlite3',
#          'NAME': BASE_DIR / 'db.sqlite3',
#      }
#  }

#  DATABASES = {
#      'default': {
#          'ENGINE': 'django.db.backends.postgresql',
#          'NAME': 'app1_db',
#          'USER': 'app1_user',
#          'PASSWORD': 'Passw0rd',
#          'HOST': '127.0.0.1',
#          'PORT': '5432',
#          'OPTIONS': {
#              'sslmode': 'require'
#          }
#      }
#  }
