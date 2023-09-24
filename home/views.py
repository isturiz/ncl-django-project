from django.shortcuts import render
from django.views.generic import TemplateView

from django.views.generic import ListView, UpdateView
from django.urls import reverse_lazy


from .models import Student
from .forms import StudentForm

from .models import Lesson
from .models import Teacher

from .models import Subscription



# Create your views here.
class HomePageView(TemplateView):
    template_name = "home.html"

class StudentListView(ListView):
    model = Student
    template_name = 'home/student_list.html'
    context_object_name = 'students' 

class StudentUpdateView(UpdateView):
    model = Student
    form_class = StudentForm
    template_name = 'forms/student_update.html'  # Nombre del archivo HTML para editar un estudiante
    success_url = '/students/'

class TeacherListView(ListView):
    model = Teacher
    template_name = 'home/teacher_list.html'
    context_object_name = 'teachers' 

class LessonListView(ListView):
    model = Lesson
    template_name = 'home/lesson_list.html'
    context_object_name = 'lessons' 

class LessonCalendarsView(TemplateView):
    template_name = 'home/lesson_calendar.html'

class SubscriptionsView(ListView):
    model = Subscription
    template_name = 'home/subscription_list.html'
    context_object_name = 'subscriptions'