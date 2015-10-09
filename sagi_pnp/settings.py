"""
Django settings for sagi_pnp project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

SECRET_KEY = 'quy5u27()-!fcih0&a*3q4wwolhb+919dj77=f3iay4ov@dqlq'

DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = ["*"]

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'ubigeo',
    'bootstrap3',
    'ayudas',
    'levantamiento',
    'reparar',
    'metrados',
    'media_objects',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'sagi_pnp.urls'

WSGI_APPLICATION = 'sagi_pnp.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'pnpsagifen',
        'USER': 'postgres',
        'PASSWORD': '12345rtfgv',
        'HOST': 'localhost',
        'PORT': '5433'
    }
}


LANGUAGE_CODE = 'es-PE'

TIME_ZONE = 'America/Lima'

USE_I18N = True

USE_L10N = True

USE_TZ = True

SITE_ID = 1

STATIC_URL = '/static/'

TEMPLATE_DIRS = [os.path.join(BASE_DIR,"templates")]

STATICFILES_DIRS = [os.path.join(BASE_DIR,"statics")]

STATIC_ROOT = os.path.join(BASE_DIR, "static")

MEDIA_ROOT = os.path.join(BASE_DIR, "medias")

MEDIA_URL = '/medias/'

LOGIN_URL = '/login/'

SESSION_COOKIE_HTTPONLY =  True

GOOGLE_MAPS_KEY = "AIzaSyC1HbAPP2McUbLS9EvG4tWQRD294vLIPr8"

STATIC_URL = '/static/'
