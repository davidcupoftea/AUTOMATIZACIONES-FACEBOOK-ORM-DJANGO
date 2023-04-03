# settings.py
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'sqlite.db',
    }
}

INSTALLED_APPS = (
    'database',
    )

SECRET_KEY = '12345'