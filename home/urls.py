from django.urls import path
from django.views.generic import TemplateView

from .views import HomePageView
from .views import StudentListView, StudentAddView, StudentUpdateView
from .views import TeacherListView, TeacherAddView, TeacherUpdateView
from .views import LessonListView, LessonCreateView, LessonUpdateView
from .views import SubscriptionView, SubscriptionCreateView, SubscriptionUpdateView
from .views import CalendarView
from .views import EventUpdateView, EventCreateView, EventLessonUpdateView

from .views import UserListView

# TODO
# Change add -> create in all urls and views


urlpatterns = [
    path("", HomePageView.as_view(), name="home"),

    path('students/', StudentListView.as_view(), name='student-list'),
    path('students/add/', StudentAddView.as_view(), name='student-add'),
    path('students/<int:pk>/', StudentUpdateView.as_view(), name='student-update'),

    path('teachers/', TeacherListView.as_view(), name='teacher-list'),
    path('teachers/add/', TeacherAddView.as_view(), name='teacher-add'),
    path('teachers/<int:pk>/', TeacherUpdateView.as_view(), name='teacher-update'),

    path('lessons/', LessonListView.as_view(), name='lesson-list'),
    path('lessons/create/', LessonCreateView.as_view(), name='lesson-create'),
    path('lessons/<int:pk>', LessonUpdateView.as_view(), name='lesson-update'),

    path('calendar/', CalendarView.as_view(), name='calendar'),
    path('event/create/', EventCreateView.as_view(), name='event-create'),
    path('event/<int:pk>/', EventLessonUpdateView.as_view(), name='event-update-form'), # update with lesson form
    path('event/update/', EventUpdateView.as_view(), name='event-update'), # resize and date with calendar

    path('subscriptions/', SubscriptionView.as_view(), name='subscription-list'),
    path('subscriptions/create/', SubscriptionCreateView.as_view(), name='subscription-create'),
    path('subscriptions/<int:pk>', SubscriptionUpdateView.as_view(), name='subscription-update'),

    path('users/', UserListView.as_view(), name='user-list'),
    
]