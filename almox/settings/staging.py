from .base import *

DEBUG = True

ALLOWED_HOSTS = ["localhost", "127.0.0.0", "127.0.0.1"]
CORS_ORIGIN_ALLOW_ALL = False
CORS_ORIGIN_WHITELIST = ("http://localhost:5000",)

# Database settings
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "USER": os.getenv("STAGE_DB_USER"),
        "PASSWORD": os.getenv("STAGE_DB_PASSWORD"),
        "NAME": os.getenv("STAGE_DB_NAME"),
        "HOST": os.getenv("STAGE_DB_HOST"),
        "PORT": os.getenv("STAGE_DB_PORT"),
        "OPTIONS": {
            "use_returning_into": False,
        },
    }
}
