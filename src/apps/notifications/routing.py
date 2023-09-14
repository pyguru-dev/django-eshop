from django.urls import path

from .consumers import (BroadcastNotificationConsumer,
                        NotificationConsumer,
                        EchoConsumer)

websocket_urlpatterns = [
    path('ws/notifications/private/', NotificationConsumer.as_asgi()),
    path('ws/notifications/broadcast/', BroadcastNotificationConsumer.as_asgi()),
    path('ws/echo/', EchoConsumer.as_asgi()),
]
