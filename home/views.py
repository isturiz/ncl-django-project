from django.shortcuts import render
from django.views.generic import TemplateView

from django.views.generic import ListView, UpdateView


from .models import Student
from .forms import StudentForm

# Create your views here.
class HomePageView(TemplateView):
    template_name = "home.html"

class StudentListView(ListView):
    model = Student
    template_name = 'home/student_list.html'

class StudentUpdateView(UpdateView):
    model = Student
    form_class = StudentForm
    template_name = 'forms/student_update.html'  # Nombre del archivo HTML para editar un estudiante
    success_url = '/students/'