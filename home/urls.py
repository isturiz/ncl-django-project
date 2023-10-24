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
from .views import Payment_ListView, Payment_CreateView, Payment_UpdateView

from .views import LessonTypes_ListView, LessonTypes_CreateView, LessonTypes_UpdateView
from .views import SubscriptionTypes_ListView, SubscriptionTypes_CreateView, SubscriptionTypes_UpdateView

from .views import load_subscriptions


from .views import UserListView

# TODO
# Change add -> create in all urls and views


urlpatterns = [
    path("", HomePageView.as_view(), name="home"),

    # Students
    path('students/', Student_ListView.as_view(), name='student-list'),
    path('students/add/', Student_CreateView.as_view(), name='student-add'),
    path('students/<int:pk>/', Student_UpdateView.as_view(), name='student-update'),
    path('students/graph/', StudentGraph_View.as_view(), name='student-graph'),

    # Teachers
    path('teachers/', TeacherListView.as_view(), name='teacher-list'),
    path('teachers/add/', TeacherAddView.as_view(), name='teacher-add'),
    path('teachers/<int:pk>/', TeacherUpdateView.as_view(), name='teacher-update'),

    # Lessons
    path('lessons/', LessonListView.as_view(), name='lesson-list'),
    path('lessons/create/', LessonCreateView.as_view(), name='lesson-create'),
    path('lessons/<int:pk>/', LessonUpdateView.as_view(), name='lesson-update'),

    # Lesson Types
    path('lesson-types/', LessonTypes_ListView.as_view(), name='lesson-types-list'),
    path('lesson-types/create/', LessonTypes_CreateView.as_view(), name='lesson-types-create'),
    path('lesson-types/<int:pk>/', LessonTypes_UpdateView.as_view(), name='lesson-types-update'),

    path('load-subscription/<int:student_id>/', load_subscriptions, name='load-subscription'),

    # Calendar
    path('calendar/', CalendarView.as_view(), name='calendar'),
    path('event/create/', EventCreateView.as_view(), name='event-create'),
    path('event/<int:pk>/', EventLessonUpdateView.as_view(), name='event-update-form'), # update with lesson form
    path('event/update/', EventUpdateView.as_view(), name='event-update'), # resize and date with calendar

    # Subscriptions
    path('subscriptions/', SubscriptionListView.as_view(), name='subscription-list'),
    path('subscriptions/create/', SubscriptionCreateView.as_view(), name='subscription-create'),
    path('subscriptions/<int:pk>/', SubscriptionUpdateView.as_view(), name='subscription-update'),

    # Subscription Types
    path('subscription-types/', SubscriptionTypes_ListView.as_view(), name='subscription-types-list'),
    path('subscription-types/create/', SubscriptionTypes_CreateView.as_view(), name='subscription-types-create'),
    path('subscription-types/<int:pk>/', SubscriptionTypes_UpdateView.as_view(), name='subscription-types-update'),

    # Finance
    path('finances/', FinanceView.as_view(), name='finances'),

    path('payments/', Payment_ListView.as_view(), name='payment-list'),
    path('payments/create/', Payment_CreateView.as_view(), name='payment-create'),
    path('payments/<int:pk>/', Payment_UpdateView.as_view(), name='payment-update'),

    # Users
    path('users/', UserListView.as_view(), name='user-list'),
    
]