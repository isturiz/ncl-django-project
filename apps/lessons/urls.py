

# accounts/urls.py
from django.urls import path
from .views import Lesson_ListView, Lesson_CreateView, Lesson_UpdateView, load_subscriptions



urlpatterns = [

    path('', Lesson_ListView.as_view(), name='lesson-list'),
    path('create/', Lesson_CreateView.as_view(), name='lesson-create'),
    path('update/<int:pk>/', Lesson_UpdateView.as_view(), name='lesson-update'),

    path('load-subscription/<int:student_id>/', load_subscriptions, name='load-subscription'),

]