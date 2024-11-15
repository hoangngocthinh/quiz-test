from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)
from django.urls import path

from authentication import views

urlpatterns = [
    path("registration/", views.RegisterApiView.as_view(), name="registration"),
    path("token/verify/", TokenVerifyView.as_view(), name="token_verify"),
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]
