DEBUG = False
ALLOWED_HOSTS = ['127.0.0.1']

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

