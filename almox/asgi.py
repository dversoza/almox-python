import os

from django.core.asgi import get_asgi_application
from dotenv import load_dotenv

load_dotenv(os.path.join(os.path.dirname(os.path.dirname(__file__)), ".env"))

application = get_asgi_application()
