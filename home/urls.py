from django.urls import path
from django.views.generic import TemplateView

from .views import HomePageView
from .views import StudentListView, StudentUpdateView
from .views import TeacherListView
from .views import LessonListView
from .views import SubscriptionsView
from .views import CalendarView



urlpatterns = [
    path("", HomePageView.as_view(), name="home"),

    path('students/', StudentListView.as_view(), name='student-list'),
    path('students/<int:pk>/', StudentUpdateView.as_view(), name='student-update'),

    path('teacher/', TeacherListView.as_view(), name='teacher-list'),

    path('lesson/', LessonListView.as_view(), name='lesson-list'),

    path('calendar/', CalendarView.as_view(), name='calendar'),

    path('subscriptions/', SubscriptionsView.as_view(), name='subscriptions-list')

    
]