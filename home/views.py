from django.shortcuts import render
from django.views.generic import TemplateView

from django.views.generic import ListView, UpdateView
from django.urls import reverse_lazy
from django.views import View
from django.views.generic.edit import CreateView

from .models import Student
from .forms import StudentForm
from .forms import EventCreateForm

from .models import Lesson
from .models import Teacher

from .models import Subscription

from .models import StudentXDetail

from django.contrib.auth.models import User

from django.http import JsonResponse, HttpResponseNotFound
from django.views.decorators.csrf import csrf_exempt

########## Calendar views ##########
class CalendarView(ListView):
    model = StudentXDetail
    # model = Subscription
    template_name = 'home/calendar.html'
    context_object_name = 'events'

class EventCreateView(CreateView):
    model = StudentXDetail
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
                event = StudentXDetail.objects.get(id=event_id)
                event.start_date = new_start_date
                event.end_date = new_end_date
                event.save()
                return JsonResponse({'status': 'success'})
            except StudentXDetail.DoesNotExist:
                return JsonResponse({'status': 'error', 'message': 'Evento no encontrado'}, status=404)
            except Exception as e:
                return JsonResponse({'status': 'error', 'message': str(e)}, status=400)
        else:
            # Si la solicitud no es POST, puedes devolver un error 405 (Method Not Allowed)
            return JsonResponse({'status': 'error', 'message': 'Método no permitido'}, status=405)


# Create your views here.
class HomePageView(TemplateView):
    template_name = "home.html"

########## Student views ##########
class StudentListView(ListView):
    model = Student
    template_name = 'home/student_list.html'
    context_object_name = 'students'

class StudentAddView(CreateView):
    model = Student
    form_class = StudentForm
    template_name = 'forms/student.html'  
    success_url = '/students/'

class StudentUpdateView(UpdateView):
    model = Student
    form_class = StudentForm
    template_name = 'forms/student.html'  
    success_url = '/students/'


########## Teacher views ##########
class TeacherListView(ListView):
    model = Teacher
    template_name = 'home/teacher_list.html'
    context_object_name = 'teachers' 


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