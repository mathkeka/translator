"""
Django settings for base project.

Generated by 'django-admin startproject' using Django 3.2.3.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path
import os
from datetime import timedelta
from decouple import config

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# # Build paths inside the project like this: BASE_DIR / 'subdir'.
# BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('DEBUG', default=True, cast=bool)


ADMIN_PROFILE = config('ADMIN_PROFILE')
MANAGER_PROFILE = config('MANAGER_PROFILE')
USER_PROFILE = config('USER_PROFILE')

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'corsheaders',
    'guardian',
    'django_twilio',
    'core',
    'security',
    'access',
    'translator'
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'base.urls'

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

WSGI_APPLICATION = 'base.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

# GAE = Google App Engine (configurações para mudar ipinterno e externo de acesso ao banco em produção)
if not os.getenv('GAE_APPLICATION', None):
    DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR + 'db.sqlite3',
    }
}
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': config('DB_NAME'),
            'USER': config('DB_USER'),
            'PASSWORD': config('DB_PASSWORD'),
            'HOST': config('DB_HOST'),
            'PORT': config('DB_PORT'),
        }
    }

AUTHENTICATION_BACKENDS = [
    'security.backends.CaseInsensitiveModelBackend',
    'django.contrib.auth.backends.ModelBackend',  # this is default
    'guardian.backends.ObjectPermissionBackend',
]

SESSION_ENGINE = "django.contrib.sessions.backends.db"

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = config('LANGUAGE_CODE')

TIME_ZONE = config('TIME_ZONE')

USE_I18N = config('USE_I18N', default=True, cast=bool)

USE_L10N = config('USE_L10N', default=True, cast=bool)

USE_TZ = config('USE_TZ', default=True, cast=bool)

LOCALE_PATHS = [
    os.path.join(os.path.dirname(os.path.realpath(__file__)),
                 'locale', 'rest_framework_simplejwt'),
]

REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'core.pagination.CustomPagination',
    'PAGE_SIZE': 10,
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    'DEFAULT_FILTER_BACKENDS': (
        'django_filters.rest_framework.DjangoFilterBackend',
    ),
}


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/
STATIC_URL = '/static/'

# SESSION AGE 2 horas (em segundos)
ALLOWED_HOSTS = config('ALLOWED_HOSTS', cast=lambda v: [s.strip() for s in v.split(',')])
SESSION_COOKIE_DOMAIN = config('SESSION_COOKIE_DOMAIN')
SESSION_COOKIE_AGE = config('SESSION_COOKIE_AGE', cast=int)
CORS_ALLOW_CREDENTIALS = config('CORS_ALLOW_CREDENTIALS', cast=bool)
CORS_ORIGIN_WHITELIST = config('CORS_ORIGIN_WHITELIST', cast=lambda v: [s.strip() for s in v.split(',')])
CSRF_COOKIE_DOMAIN = config('CSRF_COOKIE_DOMAIN')
CSRF_TRUSTED_ORIGINS = config('CSRF_TRUSTED_ORIGINS')

# Email
EMAIL_HOST = config('EMAIL_HOST', default='localhost')
EMAIL_PORT = config('EMAIL_PORT', default=25, cast=int)
EMAIL_HOST_USER = config('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD')
EMAIL_USE_TLS = config('EMAIL_USE_TLS', default=False, cast=bool)
DEFAULT_FROM_EMAIL = config('DEFAULT_FROM_EMAIL')
DEFAULT_REPLY_TO_EMAIL = config('DEFAULT_REPLY_TO_EMAIL')
NOTIFICATION_FROM = config('NOTIFICATION_FROM')
FRONTEND_DNS = config('FRONTEND_DNS')

# Tempo de validade do link de recuperação de email, em segundos: 1800 = 30 minutos
RECOVERY_THRESHOLD = config('RECOVERY_THRESHOLD', default=1800, cast=int)

# Email Notification
EMAIL_NOTIFICATION_ENABLED = config(
    'EMAIL_NOTIFICATION_ENABLED', default=True, cast=bool)
EMAIL_NOTIFICATION_DEV = config(
    'EMAIL_NOTIFICATION_DEV', default=True, cast=bool)
EMAIL_NOTIFICATION_DEV_TO = config('EMAIL_NOTIFICATION_DEV_TO')
SYSTEM_URL = config('SYSTEM_URL')
SYSTEM_NAME = config('SYSTEM_NAME')
SYSTEM_LOGO = config('SYSTEM_LOGO')

# SendGrid
SENDGRID_API_KEY = config('SENDGRID_API_KEY')

# Twilio
TWILIO_ACCOUNT_SID = config('TWILIO_ACCOUNT_SID')
TWILIO_AUTH_TOKEN = config('TWILIO_AUTH_TOKEN')
TWILIO_SENDER = config('TWILIO_SENDER')

AUTH_USER_MODEL = config('AUTH_USER_MODEL')

DEFAULT_AUTO_FIELD = config('DEFAULT_AUTO_FIELD')
STATIC_URL = config('STATIC_URL')

PARAMS = {
    'MAX_TENTATIVA_LOGIN': config('MAX_TENTATIVA_LOGIN', cast=int)
}


SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(days=config('ACCESS_TOKEN_LIFETIME', cast=int)),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=config('REFRESH_TOKEN_LIFETIME', cast=int)),
}

MAX_ATTEMPTS_LOGIN = config('MAX_ATTEMPTS_LOGIN', cast=int)
