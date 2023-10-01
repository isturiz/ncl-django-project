from django.urls import path
from django.views.generic import TemplateView

from .views import HomePageView
from .views import StudentListView, StudentUpdateView
from .views import TeacherListView
from .views import LessonListView
from .views import SubscriptionsView
from .views import CalendarView
from .views import EventUpdateView, EventCreateView

from .views import UserListView




urlpatterns = [
    path("", HomePageView.as_view(), name="home"),

    path('students/', StudentListView.as_view(), name='student-list'),
    path('students/<int:pk>/', StudentUpdateView.as_view(), name='student-update'),

    path('teachers/', TeacherListView.as_view(), name='teacher-list'),

    path('lessons/', LessonListView.as_view(), name='lesson-list'),

    path('calendar/', CalendarView.as_view(), name='calendar'),
    path('event/update/', EventUpdateView.as_view(), name='event-update'),
    path('event/create/', EventCreateView.as_view(), name='event-create'),


    path('subscriptions/', SubscriptionsView.as_view(), name='subscriptions-list'),

    path('users/', UserListView.as_view(), name='user-list'),
    
]