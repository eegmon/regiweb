from .settings import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

SECRET_KEY = 'django-insecure-&-n5u#q!qxeun&ijswu2ir(gqg_y=f)8o4pxu8_i0l+7h2#iis'

DEBUG = True