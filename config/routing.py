# Central websocket routing (future expansion)
from apps.stocks.routing import websocket_urlpatterns
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
import apps.stocks.routing


application = ProtocolTypeRouter({
    "websocket": AuthMiddlewareStack(
        URLRouter(
            apps.stocks.routing.websocket_urlpatterns
        )
    ),
})

__all__ = ["websocket_urlpatterns"]
