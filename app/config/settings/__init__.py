from os import environ

APP_ENV = environ.get("APP_ENV")

if APP_ENV == 'production':
    from .production import *
elif APP_ENV == 'staging':
    from .staging import *
elif APP_ENV == 'development':
    from .local import *
else:
    from .local import *
