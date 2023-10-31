from django.urls import path

from .views import User_ListView

urlpatterns = [
    path('', User_ListView.as_view(), name='user-list'),
]