"""
Django settings for store project.

Generated by 'django-admin startproject' using Django 4.2.1.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

import os
from pathlib import Path
import logging, django_loki

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-d2v!l(!i2z!lv1a456$jln#9!6lp008s&1#9drkik(frbrkcyr'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
# DEBUG = None

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework_swagger',
    'rest_framework',
    'my_app',
    'django_prometheus', # метрики
]

MIDDLEWARE = [
    'django_prometheus.middleware.PrometheusBeforeMiddleware', #
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django_prometheus.middleware.PrometheusAfterMiddleware', #
]

ROOT_URLCONF = 'store.urls'

TEMPLATES = [
    {
        
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'store.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django_prometheus.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

CACHES = {
    'default': {
        'BACKEND': 'django_prometheus.cache.backends.filebased.FileBasedCache',
        'LOCATION': '/var/tmp/django_cache',
    }
}

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'ru-RU'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/


STATIC_URL = '/static/'
# STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
# VENV_PATH = os.path.dirname(BASE_DIR)
# STATIC_ROOT = os.path.join(VENV_PATH, 'static_root')
# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

REST_FRAMEWORK = { 'DEFAULT_SCHEMA_CLASS': 'rest_framework.schemas.coreapi.AutoSchema' }


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters' : {
        'main_format' : {
            'format': '{asctime} - {levelname} - {module} - {filename} - {message}',
            'style': '{',
        },
        'loki': {
            'class': 'django_loki.LokiFormatter',  # required
            'format': '[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] [%(funcName)s] %(message)s',  # optional, default is logging.BASIC_FORMAT
            'datefmt': '%Y-%m-%d %H:%M:%S',  # optional, default is '%Y-%m-%d %H:%M:%S'
        },
    },
    'handlers': {
        'file': {
            # 'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'formatter' : 'main_format',
            'filename': './loggy/debug.log',
        },
        'loki': {
            'level': 'DEBUG',  # required
            'class': 'django_loki.LokiHttpHandler',  # required
            'host': 'host.docker.internal',  # required, your grafana/Loki server host, e.g:192.168.57.242
            'formatter': 'loki',  # required, loki formatter,
            'port': 3100,  # optional, your grafana/Loki server port, default is 3100
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file', 'loki'],
            'level': 'INFO',
            'propagate': False,
        },
    },
}