from .base import *
INSTALLED_APPS += ['django_extensions']

# DEBUG
# ------------------------------------------------------------------------------
# Turn debug off so tests run faster
# DEBUG = False
# TEMPLATES[0]['OPTIONS']['debug'] = False

# MYSQL_DATABASE = environ.get("MYSQL_DATABASE")
# MYSQL_USER = environ.get("MYSQL_USER")
# MYSQL_PASSWORD = environ.get("MYSQL_PASSWORD")
# MYSQL_HOSTNAME = environ.get("MYSQL_HOSTNAME")

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': MYSQL_DATABASE,
#         'USER': MYSQL_USER,
#         'PASSWORD': MYSQL_PASSWORD,
#         'HOST': MYSQL_HOSTNAME,
#         'PORT': 3306,
#     }
# }
