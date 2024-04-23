from .base import *

DEBUG = False
ALLOWED_HOSTS = []
CSRF_TRUSTED_ORIGINS = []
CORS_ALLOW_ALL_ORIGINS = False

CORS_ALLOWED_ORIGINS = [
    # testing CORS requests
    "https://www.test-cors.org",
]