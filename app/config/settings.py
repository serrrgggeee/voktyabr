from dotenv import load_dotenv
import os, sys
import logging
import datetime



BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ENV_DIR = os.path.abspath(os.path.join(BASE_DIR, os.pardir))

dotenv_path = os.path.join(ENV_DIR, '.env')
load_dotenv(dotenv_path)

SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', 'setmeinprod')

DEBUG = bool(int(os.environ.get('DJANGO_DEBUG', 0)))
ALLOWED_HOSTS = ['*'] if DEBUG else os.environ.get('DJANGO_ALLOWED_HOSTS').split(' ')
CSRF_TRUSTED_ORIGINS = os.environ.get('CSRF_TRUSTED_ORIGINS').split(' ')
CORS_ALLOW_ALL_ORIGINS = True if DEBUG else False

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'whitenoise.runserver_nostatic',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.sitemaps',
    'rest_framework',
    'mptt',
    'django_mptt_admin',
    'ckeditor',
    'ckeditor_uploader',
    'main',
    'base',
    'config',
    'easy_thumbnails',
    'article',
    'place',
    'book',
    'organisations',
    'meta',
    'enumeration',
    'photo',
    'panoram',
    'bot',
    'vk',
    'django_celery_beat',


]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,  'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'base.context_processors.common',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'


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

TIME_ZONE = 'Europe/Moscow'

USE_I18N = True

USE_L10N = True

USE_TZ = True
LANGUAGE_CODE = 'ru'


MEDIA_ROOT = os.path.join(BASE_DIR, "media")
MEDIA_URL = 'media/'

SITE_ID = 1

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static/')

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)


CKEDITOR_UPLOAD_PATH = os.path.join('uploads/')
CKEDITOR_IMAGE_BACKEND = "pillow"
CKEDITOR_CONFIGS = {
    'default': {
        'skin': 'moono',
        'toolbar_Basic': [
            ['Source', '-', 'Bold', 'Italic']
        ],
        'toolbar_YourCustomToolbarConfig': [
            {'name': 'document', 'items': ['Source', '-', 'Save', 'NewPage', 'Preview', 'Print', '-', 'Templates']},
            {'name': 'clipboard', 'items': ['Cut', 'Copy', 'Paste', 'PasteText', 'PasteFromWord', '-', 'Undo', 'Redo']},
            {'name': 'editing', 'items': ['Find', 'Replace', '-', 'SelectAll']},
            {'name': 'forms',
             'items': ['Form', 'Checkbox', 'Radio', 'TextField', 'Textarea', 'Select', 'Button', 'ImageButton',
                       'HiddenField']},
            '/',
            {'name': 'basicstyles',
             'items': ['Bold', 'Italic', 'Underline', 'Strike', 'Subscript', 'Superscript', '-', 'RemoveFormat']},
            {'name': 'paragraph',
             'items': ['NumberedList', 'BulletedList', '-', 'Outdent', 'Indent', '-', 'Blockquote', 'CreateDiv', '-',
                       'JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock', '-', 'BidiLtr', 'BidiRtl',
                       'Language']},
            {'name': 'links', 'items': ['Link', 'Unlink', 'Anchor']},
            {'name': 'insert',
             'items': ['Image', 'Flash', 'Table', 'HorizontalRule', 'Smiley', 'SpecialChar', 'PageBreak', 'Iframe']},
            '/',
            {'name': 'styles', 'items': ['Styles', 'Format', 'Font', 'FontSize']},
            {'name': 'colors', 'items': ['TextColor', 'BGColor']},
            {'name': 'tools', 'items': ['Maximize', 'ShowBlocks']},
            {'name': 'about', 'items': ['About']},
            {'name': 'yourcustomtools', 'items': [
                'Preview',
                'Maximize',

            ]},
        ],
        'toolbar': 'YourCustomToolbarConfig',
        'tabSpaces': 4,
        'extraPlugins': ','.join(
            [
                'div',
                'autolink',
                'autoembed',
                'embedsemantic',
                'autogrow',
                'widget',
                'lineutils',
                'clipboard',
                'dialog',
                'dialogui',
                'elementspath'
            ]),
    }
}

REDACTOR_OPTIONS = {'removeStyles': True, 'lang': 'en'}
REDACTOR_UPLOAD = 'media/redactor'

SUIT_CONFIG = {
    'MENU': (
        'sites',
        {'app': 'auth', 'label': 'Authorization', 'icon':'icon-lock'},
        {'app': 'auth', 'models': ('user', 'group')},
        {'label': 'Settings', 'icon':'icon-cog', 'models': ('auth.user', 'auth.group')},
        {'label': 'Custom', 'icon':None, 'models': (
            'auth.group',
            {'model': 'auth.user', 'label': 'Staff'}
        )},
        {'label': 'Users', 'url': 'auth.user', 'icon':'icon-user'},
        '-',
        {'label': 'Secure', 'permissions': 'auth.add_user', 'models': [
            {'label': 'custom-child', 'permissions': ('auth.add_user', 'auth.add_group')}
        ]},
    )
}

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(name)s.%(funcName)s:%(lineno)d %(message)s'
        }
    },
    'handlers': {
        'default': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': 'main.log',
            'maxBytes': 1024*1024*5, # 5 MB
            'formatter': 'verbose',
        },
        'sms_file': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': 'sms.log',
            'maxBytes': 1024*1024*5, # 5 MB
            'formatter': 'verbose'
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        }
    },
    'loggers': {
        '': {
            'handlers': ['default', 'console'],
            'level': 'INFO',
            'propagate': True
        },
    },
}

UPLOAD_DIR = '/home/serrrgggeee/Dropbox/октябрьский/'

CELERY_BROKER_URL = os.environ.get("CELERY_BROKER_URL")
CELERY_BEAT_SCHEDULER = 'django_celery_beat.schedulers:DatabaseScheduler'

JWT_AUTH = {
'JWT_EXPIRATION_DELTA': datetime.timedelta(days=1),
'JWT_RESPONSE_PAYLOAD_HANDLER': 'common.utilities.auth.jwt_response_payload_handler',
'JWT_AUTH_HEADER_PREFIX': 'Bearer',
'JWT_PAYLOAD_HANDLER':
'rest_framework_jwt.utils.jwt_payload_handler',
'JWT_ALLOW_REFRESH': True,

}

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ.get("POSTGRES_DB", ""),
        'USER': os.environ.get("POSTGRES_USER", ""),
        'PASSWORD':os.environ.get("POSTGRES_PASSWORD", ""),
        'PORT': os.environ.get("POSTGRES_PORT", ""),
        'HOST': os.environ.get("POSTGRES_HOST", "localhost"),
    }
}


DEFAULT_AUTO_FIELD='django.db.models.AutoField'

DATA_UPLOAD_MAX_MEMORY_SIZE = 52428800


BOT_API_TOCKEN = os.environ.get('BOT_API_TOCKEN')

