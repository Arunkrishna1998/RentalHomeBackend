"""
Django settings for rental_home project.

Generated by 'django-admin startproject' using Django 4.2.1.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path
import os
from decouple import config
from datetime import timedelta
from rest_framework.authentication import TokenAuthentication
# from dotenv import load_dotenv

# load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY =config('SECRET_KEY'),
SECRET_KEY="django-insecure-5^2sg_$1*whs70+j1kj1*1ozxp9787_zq&)b5#clrs(2@&&h1s"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG =config('DEBUG', default=False, cast=bool),

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    "daphne",
    'channels',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'corsheaders',
    'rest_framework',
    'rest_framework_simplejwt',
    'rest_framework.authtoken',
    'accounts',
    'admin_side',
    # 'realtors',
    'listings',
    # 'contacts',
    # 'notification.apps.NotificationConfig',
    # 'chatroom',
    
]

CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels.layers.InMemoryChannelLayer"
    }
}

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'rental_home.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'build')],
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

# WSGI_APPLICATION = 'rental_home.wsgi.application'
ASGI_APPLICATION = "rental_home.asgi.application"


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE':'django.db.backends.mysql',
#         # 'NAME':config('NAME'),
#         # 'USER':config('USER'), 
# 		# 'PASSWORD': config('PASSWORD'),
#         'NAME':'rental_home',
#         'USER':'root',
#         'PASSWORD':'Robin@123',
# 		'HOST':'localhost',
#  		'PORT':'3306',
#     }

# }
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

EMAIL_BACKEND=config("EMAIL_BACKEND")
EMAIL_HOST=config("EMAIL_HOST")
EMAIL_FROM=config("EMAIL_FROM")
EMAIL_HOST_USER=config("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD=config("EMAIL_HOST_PASSWORD")
EMAIL_PORT=config("EMAIL_PORT")
EMAIL_USE_TLS=config('EMAIL_USE_TLS', default=True, cast=bool)


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

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Kolkata'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/



# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'build/static')
]
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# REST_FRAMEWORK = {
#     'DEFAULT_PERMISSION_CLASSES': [
        
#         'rest_framework.permissions.IsAuthenticated'
#     ],
#     'DEFAULT_AUTHENTICATION_CLASSES': [
#         # 'rest_framework.authentication.TokenAuthentication',
#         'rest_framework_simplejwt.authentication.JWTAuthentication'
#     ],
#     'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
#     'PAGE_SIZE': 3
# }
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    )
}


CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
    
]

CORS_ALLOW_CREDENTIALS = True
CORS_ALLOW_ALL_ORIGINS = True

# CORS_ORIGIN_ALLOW_ALL = True

FILE_UPLOAD_PERMISSIONS=0o640

AUTH_USER_MODEL = 'accounts.UserAccount'



SIMPLE_JWT = {
  'ACCESS_TOKEN_LIFETIME': timedelta(minutes=1440),
  'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
  'ROTATE_REFRESH_TOKENS': False,
  'BLACKLIST_AFTER_ROTATION': True,
  'UPDATE_LAST_LOGIN': False,

  'ALGORITHM': 'HS256',
  'SIGNING_KEY': SECRET_KEY,
  'VERIFYING_KEY': None,
  'AUDIENCE': None,
  'ISSUER': None,

  'AUTH_HEADER_TYPES': ('Bearer',),
  'AUTH_HEADER_NAME': 'HTTP_AUTHORIZATION',
  'USER_ID_FIELD': 'id',
  'USER_ID_CLAIM': 'user_id',
  'USER_AUTHENTICATION_RULE': 'rest_framework_simplejwt.authentication.default_user_authentication_rule',

  'AUTH_TOKEN_CLASSES': ('rest_framework_simplejwt.tokens.AccessToken',),
  'TOKEN_TYPE_CLAIM': 'token_type',

  'JTI_CLAIM': 'jti',

  'SLIDING_TOKEN_REFRESH_EXP_CLAIM': 'refresh_exp',
  'SLIDING_TOKEN_LIFETIME': timedelta(minutes=5),
  'SLIDING_TOKEN_REFRESH_LIFETIME': timedelta(days=1),

  # custom
  'AUTH_COOKIE': 'access_token',  # Cookie name. Enables cookies if value is set.
  'AUTH_COOKIE_DOMAIN': None,     # A string like "example.com", or None for standard domain cookie.
  'AUTH_COOKIE_SECURE': False,    # Whether the auth cookies should be secure (https:// only).
  'AUTH_COOKIE_HTTP_ONLY' : True, # Http only cookie flag.It's not fetch by javascript.
  'AUTH_COOKIE_PATH': '/',        # The path of the auth cookie.
  'AUTH_COOKIE_SAMESITE': 'Lax',  # Whether to set the flag restricting cookie leaks on cross-site requests. This can be 'Lax', 'Strict', or None to disable the flag.
}



#Razorpay
RAZORPAY_KEY_ID=config("RAZORPAY_KEY_ID")
RAZORPAY_KEY_SECRET=config("RAZORPAY_KEY_SECRET")