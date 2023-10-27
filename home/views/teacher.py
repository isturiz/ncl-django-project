from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView

from home.models import Teacher
from home.forms import TeacherForm

from django.shortcuts import render

from django.contrib import messages


class TeacherListView(ListView):
    model = Teacher
    template_name = 'home/teacher_list.html'
    context_object_name = 'teachers' 

class TeacherAddView(CreateView):
    model = Teacher
    form_class = TeacherForm
    template_name = 'forms/teacher_form.html'  
    success_url = '/teachers/'

    def form_valid(self, form):
        response = super().form_valid(form)

        messages.success(self.request, 'Profesor creado exitosamente')
        return response

class TeacherUpdateView(UpdateView):
    model = Teacher
    form_class = TeacherForm
    template_name = 'forms/teacher_form.html'  
    success_url = '/teachers/'

    def form_valid(self, form):
        response = super().form_valid(form)

        messages.success(self.request, 'Datos del profesor actualizados exitosamente')
        return response