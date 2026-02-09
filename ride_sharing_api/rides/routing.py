from django.urls import path
from .consumers import RideTrackingConsumer

websocket_urlpatterns = [
    path("ws/rides/<int:ride_id>/", RideTrackingConsumer.as_asgi()),
]
