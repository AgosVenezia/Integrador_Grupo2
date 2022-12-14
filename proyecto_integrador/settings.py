"""
Django settings for proyecto_integrador project.

Generated by 'django-admin startproject' using Django 3.2.14.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-lmp6l=2!-m@_ik09346e&l+g^9^n4c&mnx7zi03k2)3yerti76'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ["lu8dcf.servehttp.com","localhost","192.168.2.109","127.0.0.1"]


# Application definition

INSTALLED_APPS = [
    # son importante que esten presentes para que se pueda administrar
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    #'django.views.static.serve',
    'grupo2',
    'api_grupo2',
    'django_extensions',
    # para poner el API
    'rest_framework',
    #'mod_wsgi.server',

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    # comparte los archivos estaticos - img css js 
    # https://stackoverflow.com/questions/5836674/why-does-debug-false-setting-make-my-django-static-files-access-fail
    'whitenoise.middleware.WhiteNoiseMiddleware', #add whitenoise

]

ROOT_URLCONF = 'proyecto_integrador.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # donde busca por defecto todos los urls 
        'DIRS': [BASE_DIR/ 'templates' ],

        'APP_DIRS': True,  # es para que busque todos los templates d e las aplicaciones instaladas
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

WSGI_APPLICATION = 'proyecto_integrador.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

# setear la base de datos de segon archivo oct 25
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'club1',
        'USER':'postgres',
        'PASSWORD': '123',
        'HOST':'127.0.0.1',
        'PORT': '5432',
    }
}


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

LANGUAGE_CODE = 'es-AR'

TIME_ZONE = 'America/Argentina/Buenos_Aires'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

#El debug esta en true, busque el directorio static dentro de las applicacion
STATIC_URL = '/static/'

#El debug true, buscar un directorio static dentro del proyecto
STATICFILES_DIRS = [
    BASE_DIR / 'static'
]

#esto se genera en producci??n y es la que deberemos 
#crear y django ira a buscar ahi 
#python manage.py collectstatic

#antes
#STATIC_ROOT = BASE_DIR / 'static_root'
STATIC_ROOT = os.path.join(BASE_DIR,'staticfiles')  # especifica root statico

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# donde vamos a ir a guardar los archivos medias debug
MEDIA_URL = "/media/"
# media para produccion

MEDIA_ROOT = os.path.join(BASE_DIR,'media')

# constante para poder almacenar los mensajes entre solicituddes en cookies
# MESSAGE_STORAGE = 'django.contrib.menssages.storage.cookie.CookieStorage'

LOGIN_URL = '/cuentas/login/'
LOGIN_REDIRECT_URL = 'inicio'
LOGOUT_REDIRECT_URL = 'inicio'
