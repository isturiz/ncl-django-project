# accounts/urls.py
from django.urls import path, include
from django.contrib.auth import views as auth_views
from .forms import CustomLoginForm
from .views import UserCreateView, UserUpdateView



urlpatterns = [
    path("login/", auth_views.LoginView.as_view(
        template_name="registration/login.html",
        authentication_form=CustomLoginForm,
    ), name="login"),

    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path('create_user/', UserCreateView.as_view(), name='create-user'),
    path('users/<int:pk>/edit/', UserUpdateView.as_view(), name='user-edit'),


]