# core/settings/developer_settings.py
from .base_settings import *


logging.info("In development 🏗️")

PASSWORD_HASHERS = [
    'django.contrib.auth.hashers.UnsaltedMD5PasswordHasher',  # Fast, insecure hasher. This speeds up your tests in development.
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': REPO_DIR / 'db.sqlite3',
    }
}

SECRET_KEY = 'django-insecure-secret-key-for-development-1234'
