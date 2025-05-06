# routing.py

from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from django.urls import path
from .consumers import TripConsumer  # Импортируем наш consumer для trip

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter([
            # Здесь мы указываем путь для подключения WebSocket
            path("ws/trip/<int:driver_id>/", TripConsumer.as_asgi()),  # Замена <int:driver_id> на правильный ID водителя
        ])
    ),
})
