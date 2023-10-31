from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView

from apps.home.models import Teacher
from apps.teachers.forms import TeacherForm

from django.shortcuts import render

from django.contrib import messages


class Teacher_ListView(ListView):
    model = Teacher
    template_name = 'home/teacher_list.html'
    context_object_name = 'teachers' 

class Teacher_CreateView(CreateView):
    model = Teacher
    form_class = TeacherForm
    template_name = 'forms/teacher_form.html'  
    success_url = '/teachers/'

    def form_valid(self, form):
        response = super().form_valid(form)

        messages.success(self.request, 'Profesor creado exitosamente')
        return response

class Teacher_UpdateView(UpdateView):
    model = Teacher
    form_class = TeacherForm
    template_name = 'forms/teacher_form.html'  
    success_url = '/teachers/'

    def form_valid(self, form):
        response = super().form_valid(form)

        messages.success(self.request, 'Datos del profesor actualizados exitosamente')
        return response