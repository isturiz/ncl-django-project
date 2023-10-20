from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView

from home.models import Lesson
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