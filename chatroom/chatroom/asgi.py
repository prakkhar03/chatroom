import os
from django.core.asgi import get_asgi_application
from channels.routing import get_default_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "chatroom.settings")

django_asgi_app = get_asgi_application()

import chatroom.routing  

application = chatroom.routing.application
