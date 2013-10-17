DEBUG = False
ALLOWED_HOSTS = ['127.0.0.1']

EMAIL_BACKEND = 'django.core.mail.backends.dummy.EmailBackend'
STATIC_URL = "/static/"
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'test.db',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}

