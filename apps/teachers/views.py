from django.views.generic import ListView, TemplateView
from django.views.generic.edit import CreateView, UpdateView

from apps.home.models import Teacher
from apps.teachers.forms import TeacherForm

from django.shortcuts import render

from django.contrib import messages

from django.db.models import Count
import json
from django.core import serializers


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
    
class TeacherGraph_View(TemplateView):
    template_name = 'home/graphs/teacher_graph.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        
        context['count_lessons_per_teacher'] = self.count_lessons_per_teacher()


        return context
    
    def count_lessons_per_teacher(self):
        # Annotate each teacher with the count of lessons they have taught
        teachers = Teacher.objects.annotate(lesson_count=Count('lesson'))

        # Create a list of dictionaries to store the results
        teacher_data = [{'teacher_name': teacher.first_name + ' ' + teacher.first_surname, 'lesson_count': teacher.lesson_count} for teacher in teachers]

        # Convert the data to JSON
        teacher_data_json = json.dumps(teacher_data)
        
        return teacher_data_json
