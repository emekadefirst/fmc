import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent

DEBUG = True

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    "daphne",
    'django.contrib.staticfiles',
    # pkgs
    "rest_framework_simplejwt",
    'rest_framework_simplejwt.token_blacklist',
    "drf_yasg",
    "rest_framework",
    "corsheaders",    
    # apps
    'user',
    'service',

]

AUTHENTICATION_BACKENDS = [
    "user.backend.CustomBackend",
    "django.contrib.auth.backends.ModelBackend",
]

AUTH_USER_MODEL = "user.User"

ROOT_URLCONF = 'server.urls'

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

WSGI_APPLICATION = 'server.wsgi.application'
ASGI_APPLICATION = "server.asgi.application"

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
SITE_ID = 1


SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'APP': {
            'client_id': os.getenv('G-CLIENT_ID'),
            'secret': os.getenv('G-CLIENT_SECRET'),
            'key': ''
        }
    }
}
LANGUAGE_CODE = 'en-us'

USE_I18N = True
USE_TZ = True

STATIC_URL = "/static/"
STATICFILES_DIRS = ["static"]
STATIC_ROOT = "staticfiles"

MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join("media")
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
