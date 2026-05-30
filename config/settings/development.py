from .base import *

DEBUG = True

CSRF_TRUSTED_ORIGINS = ["http://localhost:8000"]

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
