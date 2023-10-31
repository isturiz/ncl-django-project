from django.urls import path

from .views import Student_ListView, Student_CreateView, Student_UpdateView, StudentGraph_View

urlpatterns = [
    path('', Student_ListView.as_view(), name='student-list'),
    path('create/', Student_CreateView.as_view(), name='student-create'),
    path('update/<int:pk>/', Student_UpdateView.as_view(), name='student-update'),
    path('graph/', StudentGraph_View.as_view(), name='student-graph'),
]