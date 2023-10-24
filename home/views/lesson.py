from django.views import View
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView

from django.http import JsonResponse
import json

from home.models import Lesson, Student, Subscription
from home.forms import EventForm

class LessonListView(ListView):
    model = Lesson
    template_name = 'home/lesson_list.html'
    context_object_name = 'lessons'

class LessonCreateView(CreateView):
    model = Lesson
    form_class = EventForm
    template_name = 'forms/lesson_form.html'
    success_url = '/lessons/'

class LessonUpdateView(UpdateView):
    model = Lesson
    form_class = EventForm
    template_name = 'forms/event_create.html'  
    success_url = '/lessons/'


def load_subscriptions(request, student_id):
    student = Student.objects.get(pk=student_id)
    subscriptions = Subscription.objects.filter(student=student)

    data = {
        'subscriptions': [{'id': sub.student.pk, 'student_name': sub.student.first_name, 'sub_id': sub.pk,'name': sub.subscription_type.name} for sub in subscriptions]
    }

    return JsonResponse(data)
