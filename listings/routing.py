from django.urls import path
from . import consumers

websocket_urlpatterns = [
    path('ws/notification/<int:realtor_id>/', consumers.NotificationConsumer.as_asgi()),
]