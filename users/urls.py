from users.views import Account  # register, dashboard
from django.urls import path, include

urlpatterns = [
    path("accounts/", include("django.contrib.auth.urls")),
    path("dashboard", Account.dashboard, name="dashboard"),
    path("register", Account.register, name="register"),
]