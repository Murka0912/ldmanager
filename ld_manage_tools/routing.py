# mysite/routing.py
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path
from . import *
from django.core.asgi import get_asgi_application
application = ProtocolTypeRouter({

    "http": get_asgi_application(),
    # WebSocket chat handler
    "websocket": URLRouter([
        path(r"", get_asgi_application())
    ])
    # (your routes here)
})