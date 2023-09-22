# accounts/urls.py
from django.urls import path, include




urlpatterns = [
    # path("", HomePageView.as_view(), name="home"),
    path("accounts/", include("django.contrib.auth.urls")),
]