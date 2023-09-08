import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djshop.envs.development')

asgi_application = get_asgi_application()

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter

import apps.notifications.routing

websocket_urlpatterns = []
websocket_urlpatterns += apps.notifications.routing.websocket_urlpatterns

application = ProtocolTypeRouter({
    'http' : asgi_application,
    'websocket' : AuthMiddlewareStack({
        URLRouter(
            websocket_urlpatterns
        ),
    })
})