# """
# ASGI config for config project.

# It exposes the ASGI callable as a module-level variable named ``application``.

# For more information on this file, see
# https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
# """

# import os

# from django.core.asgi import get_asgi_application

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

# application = get_asgi_application()


# asgi.py

import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'my_project.settings')  # Замените на имя вашего проекта

application = ProtocolTypeRouter({
    "http": get_asgi_application(),  # HTTP маршрутизация
    "websocket": AuthMiddlewareStack(  # WebSocket маршрутизация с аутентификацией
        URLRouter([
            path("ws/trip/<int:driver_id>/", TripConsumer.as_asgi()),  # Настройка WebSocket маршрута
        ])
    ),
})
