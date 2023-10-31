from django.shortcuts import render
from django.http import HttpResponse
from weasyprint import HTML
import os
from django.conf import settings
from django.views.generic import ListView
from apps.home.models import Student, Teacher, Subscription, SubscriptionType, Lesson, LessonType, Payment, User

class Student_ListView(ListView):
    model = Student
    template_name = 'reports/home_lists/student_list.html'
    context_object_name = 'students'

class Teacher_ListView(ListView):
    model = Teacher
    template_name = 'reports/home_lists/teacher_list.html'
    context_object_name = 'teachers' 

class Subscription_ListView(ListView):
    model = Subscription
    template_name = 'reports/home_lists/subscription_list.html'
    context_object_name = 'subscriptions'

class SubscriptionTypes_ListView(ListView):
    model = SubscriptionType
    template_name = 'reports/home_lists/subscription_types_list.html'
    context_object_name = 'subscription_types'

class Lesson_ListView(ListView):
    model = Lesson
    template_name = 'reports/home_lists/lesson_list.html'
    context_object_name = 'lessons'

class LessonTypes_ListView(ListView):
    model = LessonType
    template_name = 'reports/home_lists/lesson_types_list.html'
    context_object_name = 'lesson_types'

class Payment_ListView(ListView):
    model = Payment
    template_name = 'reports/home_lists/payment_list.html'
    context_object_name = 'payments'

class User_ListView(ListView):
    model = User
    template_name = 'reports/home_lists/user_list.html'
    context_object_name = 'users'


def pdf_view(request):

    students = Student.objects.all()

    context = {
        'students': students,
    }
    html_string = render(request, 'reports/home_lists/student_list.html', context).content


    # Convierte el contenido HTML en PDF
    pdf = HTML(string=html_string).write_pdf()

    # Crea una respuesta HTTP con el PDF
    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = 'filename="archivo.pdf"'

    return response
