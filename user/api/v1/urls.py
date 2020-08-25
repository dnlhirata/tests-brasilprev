from django.urls import path

from .views import UserView, LoginView

urlpatterns = [
    path("", UserView.as_view(), name="user-view"),
    path("login/", LoginView.as_view(), name="login-view"),
]
