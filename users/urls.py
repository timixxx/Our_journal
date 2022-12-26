from users.views import register, dashboard
from django.urls import path, include

urlpatterns = [
    path("accounts/", include("django.contrib.auth.urls")),
    path("dashboard", dashboard, name="dashboard"),
    path("register", register, name="register"),
]