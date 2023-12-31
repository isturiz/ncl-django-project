from django.urls import path

from apps.teachers.views import Teacher_ListView, Teacher_CreateView, Teacher_UpdateView, TeacherGraph_View


urlpatterns = [
    path('', Teacher_ListView.as_view(), name='teacher-list'),
    path('create/', Teacher_CreateView.as_view(), name='teacher-create'),
    path('update/<int:pk>/', Teacher_UpdateView.as_view(), name='teacher-update'),
    path('update/<int:pk>/', Teacher_UpdateView.as_view(), name='teacher-update'),
    path('graph/', TeacherGraph_View.as_view(), name='teacher-graph'),

]