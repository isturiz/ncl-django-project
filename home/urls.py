from django.urls import path

from .views import HomePageView
from .views import StudentListView, StudentUpdateView



urlpatterns = [
    path("", HomePageView.as_view(), name="home"),

    path('students/', StudentListView.as_view(), name='student-list'),
    path('students/<int:pk>/', StudentUpdateView.as_view(), name='student-update'),
]