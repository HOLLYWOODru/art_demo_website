"""
Django settings for artifex project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

PROJECT_ROOT = os.path.dirname(__file__)
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '--$u-d&$)kb=a5fcawfqyunh_sc(^6ebr+3+vhkkzw*u^kt4&4'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

APPEND_SLASH = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'django_activeurl',

    'articles',
    'core',
    'art',
    'events',
    'registration',
    'user',
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

AUTHENTICATION_BACKENDS = (
    'registration.backend.EmailOrUsernameModelBackend',
    'django.contrib.auth.backends.ModelBackend'
)

ROOT_URLCONF = 'urls'

WSGI_APPLICATION = 'wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'database/db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# templates
TEMPLATE_DIRS = (
    os.path.join(PROJECT_ROOT, 'templates').replace('\\','/'),
)

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.core.context_processors.tz",
    "django.contrib.messages.context_processors.messages",

    'django.core.context_processors.request',

    'constance.context_processors.config',

    'context_processors.site_architecture',
)

# grid settings
ARTICLES_COUNT_ON_PAGE = 100

WORKS_COUNT_ON_PAGE = 12

EVENTS_COUNT_ON_PAGE = 20

ARTISTS_COUNT_ON_PAGE = 20

#
from articles.settings import SITE_ARCHITECTURE_ARTICLES
from core.settings import SITE_ARCHITECTURE_ARTISTS
from events.settings import SITE_ARCHITECTURE_EVENTS
from user.settings import SITE_ARCHITECTURE_USER

# site architecture (menu structure)
SITE_ARCHITECTURE = {
    'main_menu_structure' : [
        {
            'title':        'Альманах',
            'route_name':   'articles',
        },
        {
            'title':        'Галерея',
            'route_name':   'art.works',
        },
        {
            'title':        'События',
            'route_name':   'events',
        },
        {
            'title':        'Личности',
            'route_name':   'core.artists',
        }
    ],
    'menu_for_not_logged_in_user': [
        {
            'title':        'Войти',
            'route_name':   'registration.signin',
        },
        {
            'title':        'Регистрация',
            'route_name':   'registration.signup',
        },
    ],
}

SITE_ARCHITECTURE.update(SITE_ARCHITECTURE_ARTICLES)
SITE_ARCHITECTURE.update(SITE_ARCHITECTURE_ARTISTS)
SITE_ARCHITECTURE.update(SITE_ARCHITECTURE_EVENTS)
SITE_ARCHITECTURE.update(SITE_ARCHITECTURE_USER)

# static files
STATICFILES_DIRS = (
    os.path.join(PROJECT_ROOT, "static"),
)

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

# email confirmation settings
EMAIL_HOST = 'smtp.mail.ru'
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''
EMAIL_PORT = 25
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = ''

# login & logout redirect settings
LOGIN_URL = '/signin/'

# Form default errors
form_default_errors = {
    'required': 'Это поле не может быть пустым',
    'invalid': 'Использованы недопустимые символы',
    'invalid_login': 'Неверный логин или пароль',
}
