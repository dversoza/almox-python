from .base import *

DEBUG = False

ALLOWED_HOSTS = [
    "api-catedral.versoza.dev",
    "catedral.versoza.dev",
    "localhost",
    "127.0.0.0",
    "127.0.0.1",
]
CORS_ORIGIN_ALLOW_ALL = False
CORS_ORIGIN_WHITELIST = (
    "https://catedral.versoza.dev",
    "https://api-catedral.versoza.dev",
    "http://localhost:5000",
)

# Database settings
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": os.getenv("PROD_DB_NAME"),
        "USER": os.getenv("PROD_DB_USER"),
        "PASSWORD": os.getenv("PROD_DB_PASSWORD"),
        "HOST": os.getenv("PROD_DB_HOST"),
    }
}
