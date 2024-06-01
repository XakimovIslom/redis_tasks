"""
ASGI config for config project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/asgi/
"""

import os
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter
from channels.routing import URLRouter

from django.core.asgi import get_asgi_application
from django.urls import path

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")

application = get_asgi_application()


from config.consumers import YourConsumer


application = ProtocolTypeRouter(
    {
        "http": application,
        "websocket": AuthMiddlewareStack(
            URLRouter([path("ws", YourConsumer.as_asgi())])
        ),
    }
)
