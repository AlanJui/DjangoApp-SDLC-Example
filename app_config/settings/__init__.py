import os

from .base import *


#  from django.core.exceptions import ImproperlyConfigured
#
#
#  def get_env_value(env_variable):
#      try:
#          return os.environ[env_variable]
#      except KeyError:
#          error_msg = 'Set the {} environment variable'.format(env_variable)
#          raise ImproperlyConfigured(error_msg)


def get_env_value(env_variable):
    env_value = ''
    error_msg = ''

    try:
        env_value = os.environ[env_variable]
    except KeyError:
        error_msg = 'Set the {} environment variable'.format(env_variable)
    finally:
        if error_msg:
            print(error_msg)
            env_value = 'production'

        # pylint: disable=W0150
        return env_value


# Need to set APP1_DJANGO_APP environment variable in OS
APP_LIFE_CYCLE = get_env_value('APP1_DJANGO_APP')

if APP_LIFE_CYCLE == 'local':
    from .local import *
elif APP_LIFE_CYCLE == 'dev':
    from .dev import *
elif APP_LIFE_CYCLE == 'ci':
    from .ci import *
elif APP_LIFE_CYCLE == 'staging':
    from .staging import *
else:
    from .production import *
