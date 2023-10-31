from django.urls import path

from .views import CalendarView
from .views import EventUpdateView, EventCreateView, EventLessonUpdateView

urlpatterns = [
    path('', CalendarView.as_view(), name='calendar'),
    path('create/', EventCreateView.as_view(), name='event-create'),
    path('update/<int:pk>/', EventLessonUpdateView.as_view(), name='event-update-form'), # update with lesson form
    path('update/', EventUpdateView.as_view(), name='event-update'),
]