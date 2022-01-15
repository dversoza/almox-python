import os
from dotenv import load_dotenv

from django.core.asgi import get_asgi_application

load_dotenv(os.path.join(os.path.dirname(os.path.dirname(__file__)), '.env'))

application = get_asgi_application()
