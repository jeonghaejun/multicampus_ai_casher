from channels.routing import ProtocalTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from product_list.routing

application = ProtocolTypeRouter({
    'websocket' : AuthMiddlewareStack(
        URLRouter(
            product_list.routing.websocket_urlpatterns
        )
    ),
})