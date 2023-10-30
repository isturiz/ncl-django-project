from django.urls import path

from reports.views import pdf_view

from reports.views import Student_ListView, Teacher_ListView, Subscription_ListView, SubscriptionTypes_ListView, Lesson_ListView, LessonTypes_ListView, User_ListView, Payment_ListView




urlpatterns = [
    path('generate_pdf/', pdf_view, name='generate_pdf'),

    path('pdf/students/', Student_ListView.as_view(), name='report-student-list'),
    path('pdf/teachers/', Teacher_ListView.as_view(), name='report-teacher-list'),
    path('pdf/subscriptions/', Subscription_ListView.as_view(), name='report-subscription-list'),
    path('pdf/subscription-types/', SubscriptionTypes_ListView.as_view(), name='report-subscription-types-list'),
    path('pdf/lessons/', Lesson_ListView.as_view(), name='report-lesson-list'),
    path('pdf/lesson-types/', LessonTypes_ListView.as_view(), name='report-lesson-types-list'),
    path('pdf/users/', User_ListView.as_view(), name='report-user-list'),
    path('pdf/payments/', Payment_ListView.as_view(), name='report-payment-list'),



]