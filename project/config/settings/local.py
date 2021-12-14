import os
from .base import *


DEBUG = True

ALLOWED_HOSTS = ['*']

SECRET_KEY = os.getenv('SECRET_KEY',
                       'lc8tr(l91x8b5ts#$thna%aszd6-%f22*_sn(62so+sft1s%_e')


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
    ],
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer',
    )
}