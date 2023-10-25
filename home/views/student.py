
from django.views.generic import ListView, TemplateView
from django.views.generic.edit import CreateView, UpdateView

from home.models import Student, Subscription, ActivityLog
from home.forms.student import StudentForm

from .utils.student_utils import get_start_dates_for_students

from datetime import datetime
from django.db.models import Count
from django.db.models.functions import ExtractYear
import json
from django.db.models import Sum, F



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

    def form_valid(self, form):
        # Obten el objeto Student actual y el objeto original
        student = form.instance
        original_student = Student.objects.get(pk=student.pk)

        # Compara los campos para detectar cambios
        changes = []
        if student.nombre != original_student.first_name:
            changes.append(f'Nombre: "{original_student.nombre}" a "{student.nombre}"')
        # Agrega más campos aquí para detectar otros cambios

        # Registra los cambios en el registro de actividad
        if changes:
            action_description = f"Modificación de {student}"
            action_description += "\nCambios: " + ", ".join(changes)
            ActivityLog.objects.create(user=self.request.user, action=action_description)

        return super().form_valid(form)

class StudentGraph_View(TemplateView):
    template_name = 'home/student_graph.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        start_dates = get_start_dates_for_students()

        context['start_dates'] = start_dates
        context['calculate_age_by_count'] = self.get_calculate_age_by_count()
        context['student_count_by_subscription_type'] = self.get_student_count_by_subscription_type()
        context['student_count_by_subscription_type_current_year'] = self.get_student_count_by_subscription_type_current_year()
        context['revenue_by_subscription_type_current_year'] = self.get_revenue_by_subscription_type_current_year()
        return context
    
    def get_calculate_age_by_count(self):
        today = datetime.now()

        # Calculate the age of the students and group by age
        students = Student.objects.annotate(age=ExtractYear(today) - ExtractYear('birthdate')).values('age').annotate(count=Count('id')).order_by('age')

        # Prepape the data in the desired format
        age_data = [{'age': student['age'], 'count': student['count']} for student in students]
        age_data_json = json.dumps(age_data)

        return age_data_json
    
    def get_student_count_by_subscription_type(self):

        subscription_counts = Student.objects.exclude(subscription__isnull=True).values('subscription__subscription_type__name').annotate(count=Count('id')).order_by('subscription__subscription_type__name')

        # Prepape the data in the desired format
        subscription_data = [{'subscription_type': item['subscription__subscription_type__name'], 'count': item['count']} for item in subscription_counts]

        subscription_data_json = json.dumps(subscription_data)
        return subscription_data_json
    
    def get_student_count_by_subscription_type_current_year(self):
        current_year = datetime.now().year

        subscription_counts = Student.objects.filter(subscription__start_date__year=current_year).values('subscription__subscription_type__name').annotate(count=Count('id')).order_by('subscription__subscription_type__name')

        # Prepara los datos en el formato deseado
        subscription_data = [{'subscription_type': item['subscription__subscription_type__name'], 'count': item['count']} for item in subscription_counts]

        # Convierte los datos a formato JSON
        subscription_data_json = json.dumps(subscription_data)
        return subscription_data_json
    
    def get_revenue_by_subscription_type_current_year(self):

        # Obtén el año actual
        current_year = datetime.now().year

        # Realiza la consulta para calcular las ganancias por tipo de suscripción de este año
        subscription_revenue = Subscription.objects.filter(start_date__year=current_year).values('subscription_type__name').annotate(revenue=Sum(F('subscription_type__price'))).order_by('subscription_type__name')

        # Prepara los datos en el formato deseado
        # revenue_data = [{'subscription_type': item['subscription_type__name'], 'revenue': item['revenue']} for item in subscription_revenue]
        revenue_data = [{'subscription_type': item['subscription_type__name'], 'revenue': float(item['revenue'])} for item in subscription_revenue]

        # Convierte los datos a formato JSON
        revenue_data_json = json.dumps(revenue_data)

        # Devuelve los datos en formato JSON
        return revenue_data_json