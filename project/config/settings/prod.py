from .base import *

DEBUG = False

ALLOWED_HOSTS = ['*']


DATABASES = {
     'default': {
         'ENGINE': 'django.db.backends.postgresql_psycopg2',
         'NAME': os.getenv('DB_APP','app_db'),
         'USER': os.getenv('DB_USER','admin'),
         'PASSWORD': os.getenv('DB_PASSWORD','devpass'),
         'HOST': os.getenv("DB_HOST","postgresdb"),
         'PORT': os.getenv("DB_PORT","5432"),
     }
}

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
    ],
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
        # 'rest_framework.renderers.BrowsableAPIRenderer',
    )
}