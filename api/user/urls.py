from django.urls import path
from user import views

urlpatterns = [
    path("", views.UserViewAPI.as_view(), name="create-list-user"),
    path("me/", views.MyProfileViewAPI.as_view(), name="get-my-profile"),
    path(
        "<int:pk>/",
        views.UserDetailView.as_view(),
        name="user-detail",
    ),
]
