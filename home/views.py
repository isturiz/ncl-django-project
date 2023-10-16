from django.shortcuts import render
from django.views.generic import TemplateView

from django.views.generic import ListView, UpdateView
from django.urls import reverse_lazy
from django.views import View
from django.views.generic.edit import CreateView

# Models
from .models import Student
from .models import Lesson
from .models import Teacher
from .models import Subscription
from .models import Lesson




# Forms
from .forms import StudentForm
from .forms import TeacherForm
from .forms import EventCreateForm

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

    def test_func(self):
        return self.request.user.groups.filter(name='Teachers').exists()

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


########## Subscription views ##########
class SubscriptionsView(ListView):
    model = Subscription
    template_name = 'home/subscription_list.html'
    context_object_name = 'subscriptions'


########## User views ##########
class UserListView(ListView):
    model = User
    template_name = 'home/user_list.html'
    context_object_name = 'users'