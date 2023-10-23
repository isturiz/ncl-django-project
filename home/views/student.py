
from django.views.generic import ListView, TemplateView
from django.views.generic.edit import CreateView, UpdateView

from home.models import Student
from home.forms.student import StudentForm

from .utils.student_utils import get_start_dates_for_students

from datetime import datetime
from django.db.models import Count
from django.db.models.functions import ExtractYear
import json

class Student_ListView(ListView):
    model = Student
    template_name = 'home/student_list.html'
    context_object_name = 'students'

class Student_CreateView(CreateView):
    model = Student
    form_class = StudentForm
    template_name = 'forms/student_form.html'  
    success_url = '/students/'

class Student_UpdateView(UpdateView):
    model = Student
    form_class = StudentForm
    template_name = 'forms/student_form.html'  
    success_url = '/students/'

class StudentGraph_View(TemplateView):
    template_name = 'home/student_graph.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        start_dates = get_start_dates_for_students()

        context['start_dates'] = start_dates
        context['calculate_age_by_count'] = self.calculate_age_by_count()
        return context
    
    def calculate_age_by_count(self):
        today = datetime.now()

        # Calcula la edad de los estudiantes y agrupa por edades
        students = Student.objects.annotate(age=ExtractYear(today) - ExtractYear('birthdate')).values('age').annotate(count=Count('id')).order_by('age')

        # Prepara los datos en el formato deseado
        age_data = [{'age': student['age'], 'count': student['count']} for student in students]

        # Convierte los datos a formato JSON
        age_data_json = json.dumps(age_data)

        # Devuelve los datos en formato JSON
        return age_data_json
