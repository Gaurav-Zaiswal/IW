# this file contains only those settings which are used in PRODUCTION
# and extends base.py settings, which has all the default settings

from Blog.settings.base import *
from Blog.settings.third_party import *


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

# replace ip-address and www.website-name.com with respective values
# also put same website name in database['host'], see below database settings
ALLOWED_HOSTS = ['ip-address', 'www.website-name.com']

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'news_entertainment',
        'USER': 'gaurav_jaiswal',
        'PASSWORD': 'Kapaltrika#!79',
        'HOST': 'localhost',
        'PORT': '',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]
