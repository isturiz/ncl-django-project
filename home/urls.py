from django.urls import path
from django.views.generic import TemplateView

from .views import HomePageView
from .views import StudentListView, StudentUpdateView
from .views import EducatorListView
from .views import LessonListView, LessonCalendarsView


urlpatterns = [
    path("", HomePageView.as_view(), name="home"),

    path('students/', StudentListView.as_view(), name='student-list'),
    path('students/<int:pk>/', StudentUpdateView.as_view(), name='student-update'),

    path('educator/', EducatorListView.as_view(), name='educator-list'),

    path('lesson/', LessonListView.as_view(), name='lesson-list'),
    path('lesson-calendar/', LessonCalendarsView.as_view(), name='lesson-calendar'),
    
]