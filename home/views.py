from django.shortcuts import render
from django.views.generic import TemplateView

from django.views.generic import ListView, UpdateView
from django.urls import reverse_lazy
from django.views import View
from django.views.generic.edit import CreateView

from django.core.serializers import serialize
from django.db import models
from datetime import datetime, timedelta
# Models
from .models import Student
from .models import Lesson
from .models import Teacher
from .models import Subscription
from .models import Lesson
from .models import Payment

import json
from django.db.models import Sum, functions
from django.db.models.functions import ExtractMonth



# Forms
from .forms import StudentForm
from .forms import TeacherForm
from .forms import EventCreateForm
from .forms import SubscriptionCreateForm

from django.contrib.auth.models import User

from django.http import JsonResponse, HttpResponseNotFound
from django.views.decorators.csrf import csrf_exempt

########## Calendar views ##########

class CalendarView(ListView):
    model = Lesson
    # model = Subscription
    template_name = 'home/calendar.html'
    context_object_name = 'events'

class EventCreateView(CreateView):
    model = Lesson
    form_class = EventCreateForm
    template_name = 'forms/event_create.html'
    success_url = reverse_lazy('calendar')

class EventLessonUpdateView(UpdateView):
    model = Lesson
    form_class = EventCreateForm
    template_name = 'forms/event_create.html'  
    success_url = reverse_lazy('calendar')
        
class EventUpdateView(View):
    def post(self, request):
        if request.method == 'POST':
            event_id = request.POST.get('event_id')
            new_start_date = request.POST.get('new_start_date')
            new_end_date = request.POST.get('new_end_date')

            try:
                event = Lesson.objects.get(id=event_id)
                event.start_date = new_start_date
                event.end_date = new_end_date
                event.save()
                return JsonResponse({'status': 'success'})
            except Lesson.DoesNotExist:
                return JsonResponse({'status': 'error', 'message': 'Evento no encontrado'}, status=404)
            except Exception as e:
                return JsonResponse({'status': 'error', 'message': str(e)}, status=400)
        else:
            # Si la solicitud no es POST, puedes devolver un error 405 (Method Not Allowed)
            return JsonResponse({'status': 'error', 'message': 'Método no permitido'}, status=405)


########## Home views ##########
class HomePageView(TemplateView):
    template_name = "home.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Obtener información de los modelos
        students = Student.objects.all()

        # Agregar la información al contexto
        context['students'] = students

        # También puedes agregar formularios al contexto si es necesario
        context['student_form'] = StudentForm()

        return context

########## Student views ##########
from django.contrib.auth.mixins import UserPassesTestMixin
class StudentListView(ListView):
    model = Student
    template_name = 'home/student_list.html'
    context_object_name = 'students'

class StudentAddView(CreateView):
    model = Student
    form_class = StudentForm
    template_name = 'forms/student_form.html'  
    success_url = '/students/'

class StudentUpdateView(UpdateView):
    model = Student
    form_class = StudentForm
    template_name = 'forms/student_form.html'  
    success_url = '/students/'


########## Teacher views ##########
class TeacherListView(ListView):
    model = Teacher
    template_name = 'home/teacher_list.html'
    context_object_name = 'teachers' 

class TeacherAddView(CreateView):
    model = Teacher
    form_class = TeacherForm
    template_name = 'forms/teacher_form.html'  
    success_url = '/teachers/'

class TeacherUpdateView(UpdateView):
    model = Teacher
    form_class = TeacherForm
    template_name = 'forms/teacher_form.html'  
    success_url = '/teachers/'


########## Lesson views ##########
class LessonListView(ListView):
    model = Lesson
    template_name = 'home/lesson_list.html'
    context_object_name = 'lessons'

class LessonCreateView(CreateView):
    model = Lesson
    form_class = EventCreateForm
    template_name = 'forms/lesson_form.html'
    success_url = '/lessons/'

class LessonUpdateView(UpdateView):
    model = Lesson
    form_class = EventCreateForm
    template_name = 'forms/event_create.html'  
    success_url = '/lessons/'


########## Subscription views ##########
class SubscriptionView(ListView):
    model = Subscription
    template_name = 'home/subscription_list.html'
    context_object_name = 'subscriptions'

class SubscriptionCreateView(CreateView):
    model = Subscription
    form_class = SubscriptionCreateForm
    template_name = 'forms/subscription_form.html'
    success_url = '/subscriptions/'

class SubscriptionUpdateView(UpdateView):
    model = Subscription
    form_class = SubscriptionCreateForm
    template_name = 'forms/subscription_form.html'  
    success_url = '/subscriptions/'


########## Finance views ##########
class FinanceView(TemplateView):
    template_name = 'home/finance.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        ### Payments info
        context['payment_data'] = self.get_all_payment_data()
        context['percentage_change'] = self.calculate_percentage_change()

        # Total amount per month
        context['total_payments_current_year'] = self.get_total_payments_current_year() 
        context['total_payments_amount_last_three_months'] = self.get_total_payments_amount_last_three_months() 
        context['total_payments_amount_last_six_months'] = self.get_total_payments_amount_last_six_months() 
        context['total_payments_amount_last_nine_months'] = self.get_total_payments_amount_last_nine_months() 

        # Data per month
        context['monthly_payment_data'] = self.get_monthly_payment_data_current_year()
        context['payments_data_last_three_months'] = self.get_total_payments_last_three_months()
        context['payments_data_last_six_months'] = self.get_total_payments_last_six_months()
        context['payments_data_last_nine_months'] = self.get_total_payments_last_nine_months()

        ### Students info
        context['inscription_students'] = self.get_start_dates_for_students()

        return context

    def get_start_dates_for_students(self):
        # Obtener todos los estudiantes
        students = Student.objects.all()
        
        # Crear una lista para almacenar las fechas de inicio de los estudiantes
        start_dates = []

        # Recorrer todos los estudiantes y obtener sus fechas de inicio
        for student in students:
            subscriptions = Subscription.objects.filter(student=student).order_by('start_date')
            if subscriptions.exists():
                first_subscription = subscriptions.first()
                start_dates.append({
                    'student_name': str(student),
                    'start_date': first_subscription.start_date,
                })
        
        return start_dates
    
    def get_total_payments_historically(self):
        total_payments = Payment.objects.aggregate(total=models.Sum('price'))
        return total_payments['total'] or 0

    # Total payments amount for current year
    def get_total_payments_current_year(self):
        current_year = datetime.now().year
        total_payments = Payment.objects.filter(date__year=current_year).aggregate(total=Sum('price'))
        return total_payments['total'] or 0

    # Total payments amount for last three months
    def get_total_payments_amount_last_three_months(self):
        today = datetime.now()
        three_months_ago = today - timedelta(days=90)
        total_payments = Payment.objects.filter(date__range=[three_months_ago, today]).aggregate(total=Sum('price'))

        return total_payments['total'] or 0
    
    # Total payments amount for last six months
    def get_total_payments_amount_last_six_months(self):
        today = datetime.now()
        six_months_ago = today - timedelta(days=180)
        total_payments = Payment.objects.filter(date__range=[six_months_ago, today]).aggregate(total=Sum('price'))

        return total_payments['total'] or 0
    
    # Total payments amount for last three months
    def get_total_payments_amount_last_nine_months(self):
        today = datetime.now()
        nine_months_ago = today - timedelta(days=270)
        total_payments = Payment.objects.filter(date__range=[nine_months_ago, today]).aggregate(total=Sum('price'))

        return total_payments['total'] or 0


    def get_all_payment_data(self):
        payments = Payment.objects.all()
        payment_data = [
            {
                'price': float(payment.price),
                'subscription': str(payment.subscription),
                'date': payment.date.strftime("%Y-%m-%d %H:%M:%S")
            } for payment in payments
        ]
        return json.dumps(payment_data)

    # Payment data for each month of current year
    def get_monthly_payment_data_current_year(self):
        current_year = datetime.now().year
        monthly_payments = Payment.objects.filter(date__year=current_year) \
            .annotate(month=functions.ExtractMonth('date')) \
            .values('month') \
            .annotate(total=Sum('price'))
        monthly_payment_data = [
            {
                'month': payment['month'],
                'total': float(payment['total'] or 0)
            }
            for payment in monthly_payments
        ]
        return json.dumps(monthly_payment_data)
    
    # Payment data for last three months of current year
    def get_total_payments_last_three_months(self):
        today = datetime.now()
        three_months_ago = today - timedelta(days=90)

        monthly_payments = Payment.objects.filter(date__range=[three_months_ago, today]) \
            .annotate(month=functions.ExtractMonth('date')) \
            .values('month') \
            .annotate(total=Sum('price'))

        monthly_payment_data = [
            {
                'month': payment['month'],
                'total': float(payment['total'] or 0)
            }
            for payment in monthly_payments
        ]
        
        return json.dumps(monthly_payment_data)
    
    # Payment data for last six months of current year
    def get_total_payments_last_six_months(self):
        today = datetime.now()
        six_months_ago = today - timedelta(days=180)

        monthly_payments = Payment.objects.filter(date__range=[six_months_ago, today]) \
            .annotate(month=ExtractMonth('date')) \
            .values('month') \
            .annotate(total=Sum('price'))

        monthly_payment_data = [
            {
                'month': payment['month'],
                'total': float(payment['total'] or 0)
            }
            for payment in monthly_payments
        ]
        return json.dumps(monthly_payment_data)
    
    # Payment data for last nine months of current year
    def get_total_payments_last_nine_months(self):
        today = datetime.now()
        nine_months_ago = today - timedelta(days=270)  

        monthly_payments = Payment.objects.filter(date__range=[nine_months_ago, today]) \
            .annotate(month=ExtractMonth('date')) \
            .values('month') \
            .annotate(total=Sum('price'))

        monthly_payment_data = [
            {
                'month': payment['month'],
                'total': float(payment['total'] or 0)
            }
            for payment in monthly_payments
        ]
        return json.dumps(monthly_payment_data)
    
    
    # All payment data for each month historically
    def get_monthly_payment_data_historical_month(self):
        monthly_payments = Payment.objects.annotate(month=models.functions.ExtractMonth('date')) \
            .annotate(month=functions.ExtractMonth('date')) \
            .values('month') \
            .annotate(total=Sum('price'))
        monthly_payment_data = [
            {
                'month': payment['month'],
                'total': float(payment['total'] or 0)
            }
            for payment in monthly_payments
        ]
        return json.dumps(monthly_payment_data)
    
    # Calculate percentage change per last month 
    def calculate_percentage_change(self):
        today = datetime.now()
        this_month_payments = Payment.objects.filter(date__month=today.month, date__year=today.year).aggregate(total=Sum('price'))['total'] or 0
        last_month = today - timedelta(days=today.day)
        last_month_payments = Payment.objects.filter(date__month=last_month.month, date__year=last_month.year).aggregate(total=Sum('price'))['total'] or 0
        if last_month_payments > 0:
            return round(((this_month_payments - last_month_payments) / last_month_payments) * 100, 2)
        else:
            return 0


        

########## User views ##########
class UserListView(ListView):
    model = User
    template_name = 'home/user_list.html'
    context_object_name = 'users'