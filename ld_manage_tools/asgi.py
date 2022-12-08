"""
ASGI config for untitled10 project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
"""

import os
from channels.routing import ProtocolTypeRouter
from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'untitled10.settings')
application = ProtocolTypeRouter({
  "http": get_asgi_application(),
  ## IMPORTANT::Just HTTP for now. (We can add other protocols later.)
})

