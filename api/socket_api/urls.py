# routing.py
from django.urls import path
from . import consumers

websocket_urlpatterns = [
    path("ws/quiz/<int:session_id>/leaderboard/", consumers.LeaderboardConsumer.as_asgi()),
]
