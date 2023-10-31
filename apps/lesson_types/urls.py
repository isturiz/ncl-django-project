
from django.urls import path

from .views import LessonTypes_ListView, LessonTypes_CreateView, LessonTypes_UpdateView

urlpatterns = [

    path('', LessonTypes_ListView.as_view(), name='lesson-types-list'),
    path('create/', LessonTypes_CreateView.as_view(), name='lesson-types-create'),
    path('update/<int:pk>/', LessonTypes_UpdateView.as_view(), name='lesson-types-update'),

]