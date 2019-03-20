from .base import *  # noqa
INSTALLED_APPS += ['django_extensions']

# DEBUG
# ------------------------------------------------------------------------------
# Turn debug off so tests run faster
DEBUG = False
# TEMPLATES[0]['OPTIONS']['debug'] = False
