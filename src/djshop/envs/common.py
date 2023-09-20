from import_export.formats.base_formats import CSV, XLSX, XLS, JSON
import os
import sys
from pathlib import Path
from django.conf import settings
from os.path import join
from decouple import config


# Build paths inside the project like this: BASE_DIR / 'subdir'.
PROJECT_ROOT = os.path.dirname(__file__)

BASE_DIR = Path(__file__).resolve().parent.parent
BASE_BASE_DIR = Path(__file__).resolve().parent.parent.parent
TEMPLATE_DIR = str(BASE_BASE_DIR.joinpath('templates/djshop/'))

sys.path.insert(0, join(PROJECT_ROOT, "apps"))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-^q52bhy0%%xi(h9rf4ow=7h*^$8y49+g+ig#8_hx7fnba-i^h*'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

# SECURE_SSL_REDIRECT=True

# Application definition

INSTALLED_APPS = [
    "daphne",
    "admin_interface",
    "colorfield",
    "admin_notification",

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sitemaps',
    'django.contrib.humanize',
    'django.contrib.postgres',

    # Local apps
    'apps.core.apps.CoreConfig',
    'apps.accounts.apps.AccountsConfig',
    'apps.shop.apps.ShopConfig',
    'apps.blog.apps.BlogConfig',
    'apps.api.apps.ApiConfig',
    'apps.pages.apps.PagesConfig',
    'apps.payments.apps.PaymentsConfig',
    'apps.friendships.apps.FriendshipConfig',
    'apps.shortener.apps.ShortenerConfig',
    'apps.notifications.apps.NotificationsConfig',
    'apps.vendors.apps.VendorsConfig',



    # Third-party apps
    'channels',
    'rest_framework',
    'rest_framework_simplejwt',
    'corsheaders',
    'ckeditor',
    "django_unicorn",
    'import_export',
    "debug_toolbar",
    'treebeard',
    'drf_spectacular',
    'jalali_date',
    "graphene_django",
    "graphql_auth",
    'taggit',
    'django_cleanup.apps.CleanupConfig',
    "django_filters",
    'utils',
]

MIDDLEWARE = [
    # "django.middleware.cache.UpdateCacheMiddleware",

    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # 'django.middleware.locale.LocaleMiddleware'

    "debug_toolbar.middleware.DebugToolbarMiddleware",

    # "django.middleware.cache.FetchFromCacheMiddleware",
]

ROOT_URLCONF = 'djshop.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATE_DIR],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',

                # 'apps.blog.context_processors.blog_categories',
                # 'apps.shop.context_processors.product_categories',
                # 'apps.shop.context_processors.cart',
                # 'apps.shop.context_processors.cart_total',
            ],
        },
    },
]

WSGI_APPLICATION = 'djshop.wsgi.application'
ASGI_APPLICATION = 'djshop.asgi.application'

CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels_redis.core.RedisChannelLayer",
        "CONFIG": {
            "hosts": [("127.0.0.1", 6379)],
        },
    },
}

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    },
    'postgres':  {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': '',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    },
    'mongodb': {}
}

# DATABASE_ROUTERS=['routers.db_routers.AuthRouter']

INTERNAL_IPS = [
    # ...
    "127.0.0.1",
    # ...
]


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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

LANGUAGE_CODE = 'fa-IR'

TIME_ZONE = 'Asia/Tehran'


# import locale
# locale.setlocale(locale.LC_ALL, "fa_IR.UTF-8")

USE_I18N = True

USE_TZ = True


STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static/')
# STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
STATICFILES_DIRS = [str(BASE_BASE_DIR.joinpath('static/djshop/'))]

MEDIA_URL = 'media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')

CKEDITOR_UPLOAD_PATH = "uploads/"

LOGIN_REDIRECT_URL = 'home_view'
LOGOUT_REDIRECT_URL = 'home_view'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTH_USER_MODEL = 'accounts.User'

DEFAULT_FROM_EMAIL = "info@djshop.com"
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
EMAIL_HOST = 'localhost'
EMAIL_POST = 25
# EMAIL_HOST_USER = config('')
EMAIL_HOST_PASSWORD = ''
EMAIL_USE_TLS = True


REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        # 'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly',
        # 'rest_framework.permissions.IsAuthenticatedOrReadOnly',
    ],

    'DEFAULT_AUTHENTICATION_CLASSES': [
        # 'rest_framework.authentication.TokenAuthentication',
        # 'rest_framework.authentication.SessionAuthentication',
        'rest_framework_simplejwt.authentication.JWTAuthentication',
        
    ],


    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 24
}

SPECTACULAR_SETTINGS = {
    'TITLE': 'DJShop API',
    'DESCRIPTION': 'Your project description',
    'VERSION': '1.0.0',
    'SERVE_INCLUDE_SCHEMA': False,
    # OTHER SETTINGS
}

CACHES = {
    "default": {
        # "BACKEND": "django.core.cache.backends.redis.RedisCache",
        # "LOCATION": "redis://127.0.0.1:6379",
        # "LOCATION": "redis://username:password@127.0.0.1:6379",

        # "BACKEND": "django.core.cache.backends.filebased.FileBasedCache",
        # "LOCATION": "c:/foo/bar",

        "BACKEND": "django.core.cache.backends.dummy.DummyCache",

        # "BACKEND": "django_redis.cache.RedisCache",
        # "LOCATION": "redis://127.0.0.1:6379/1",
        # "OPTIONS": {
        #     "CLIENT_CLASS": "django_redis.client.DefaultClient",
        # "COMPRESSOR": "django_redis.compressors.zlib.ZlibCompressor",
        # }
    }
}

CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'full',
        'toolbar_Custom': [
            ['Bold', 'Italic', 'Underline'],
            ['NumberedList', 'BulletedList', '-', 'Outdent', 'Indent', '-',
                'JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock'],
            ['Link', 'Unlink'],
            ['RemoveFormat', 'Source']
        ],
        'extraPlugins': ','.join([
            'uploadimage',  # the upload image feature
            # your extra plugins here
            'div',
            'autolink',
            'autoembed',
            'embedsemantic',
            'autogrow',
            # 'devtools',
            'widget',
            'lineutils',
            'clipboard',
            'dialog',
            'dialogui',
            'elementspath'
        ]),
        # 'height': 300,
        # 'width': 300,
    },
}

# CKEDITOR_RESTRICT_BY_USER = True

JALALI_DATE_DEFAULTS = {
    'Strftime': {
        'date': '%y/%m/%d',
        'datetime': '%H:%M:%S _ %y/%m/%d',
    },
    'Static': {
        'js': [
            # loading datepicker
            'admin/js/django_jalali.min.js',
            # OR
            # 'admin/jquery.ui.datepicker.jalali/scripts/jquery.ui.core.js',
            # 'admin/jquery.ui.datepicker.jalali/scripts/calendar.js',
            # 'admin/jquery.ui.datepicker.jalali/scripts/jquery.ui.datepicker-cc.js',
            # 'admin/jquery.ui.datepicker.jalali/scripts/jquery.ui.datepicker-cc-fa.js',
            # 'admin/js/main.js',
        ],
        'css': {
            'all': [
                'admin/jquery.ui.datepicker.jalali/themes/base/jquery-ui.min.css',
            ]
        }
    },
}

IMPORT_EXPORT_FORMATS = [CSV]

GRAPHENE = {
    "SCHEMA": "apps.core.schema.schema"
}

CELERY_TIMEZONE = TIME_ZONE
CELERY_ENABLE_UTC = True
CELERY_TASK_TRACK_STARTED = True
CELERY_TASK_TIME_LIMIT = 30 * 60
# CELERY_BROKER_URL = broker_url = 'amqp://myuser:mypassword@localhost:5672/myvhost'
CELERY_BROKER_URL = 'redis://localhost:6379'
CELERY_RESULT_BACKEND = CELERY_BROKER_URL
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TASK_DEFAULT_QUEUE = 'default'


TAGGIT_CASE_INSENSITIVE = True

X_FRAME_OPTIONS = "SAMEORIGIN"
SILENCED_SYSTEM_CHECKS = ["security.W019"]

NOTIFICATION_MODEL = 'pages.ContactModel'

# SESSION_ENGINE = "django.contrib.sessions.backends.cache"
# SESSION_CACHE_ALIAS = "default"
