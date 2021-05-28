"""
ASGI config for mysite project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from django.conf.urls import urlpatterns

from product_list.consumers import PresentUpload

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')

application = ProtocalTypeRouter({
    # 기존 HTTP request aplication
    "http": get_asgi_application()

    # Websocket handler
    "websocket": AuthMiddlewareStack(
        URLRouter([
            url(r"^product_list/admin/$", PresentUpload.as_asgi()),
        ])
    ),

})


