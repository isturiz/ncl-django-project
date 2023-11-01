from django.urls import path

from .views import Student_ListView, Student_CreateView, Student_UpdateView, StudentGraph_View, DetailedReportStudentView

from .views import get_subscriptions, get_lessons



# TODO
# -[ ] Change kebab-case to snake_case 



urlpatterns = [
    path('', Student_ListView.as_view(), name='student-list'),
    path('create/', Student_CreateView.as_view(), name='student-create'),
    path('update/<int:pk>/', Student_UpdateView.as_view(), name='student-update'),
    path('graph/', StudentGraph_View.as_view(), name='student-graph'),
    path('detailed_report/', DetailedReportStudentView.as_view(), name='student_detailed_report'),

    # API
    path('get_subscriptions/', get_subscriptions, name='get_subscriptions'),
    path('get_lessons/', get_lessons, name='get_lessons'),

]