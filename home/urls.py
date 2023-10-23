from django.urls import path
from django.views.generic import TemplateView

from .views import HomePageView
from .views import Student_ListView, Student_CreateView, Student_UpdateView, StudentGraph_View
from .views import TeacherListView, TeacherAddView, TeacherUpdateView
from .views import LessonListView, LessonCreateView, LessonUpdateView
from .views import SubscriptionListView, SubscriptionCreateView, SubscriptionUpdateView
from .views import CalendarView
from .views import EventUpdateView, EventCreateView, EventLessonUpdateView
from .views import FinanceView
from .views import PaymentListView, PaymentCreateView, PaymentUpdateView



from .views import UserListView

# TODO
# Change add -> create in all urls and views


urlpatterns = [
    path("", HomePageView.as_view(), name="home"),

    path('students/', Student_ListView.as_view(), name='student-list'),
    path('students/add/', Student_CreateView.as_view(), name='student-add'),
    path('students/<int:pk>/', Student_UpdateView.as_view(), name='student-update'),
    path('students/graph/', StudentGraph_View.as_view(), name='student-graph'),

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

    path('subscriptions/', SubscriptionListView.as_view(), name='subscription-list'),
    path('subscriptions/create/', SubscriptionCreateView.as_view(), name='subscription-create'),
    path('subscriptions/<int:pk>', SubscriptionUpdateView.as_view(), name='subscription-update'),

    path('finances/', FinanceView.as_view(), name='finances'),

    path('payments/', PaymentListView.as_view(), name='payment-list'),
    path('payments/create/', PaymentCreateView.as_view(), name='payment-create'),
    path('payments/<int:pk>', PaymentUpdateView.as_view(), name='payment-update'),

    path('users/', UserListView.as_view(), name='user-list'),
    
]