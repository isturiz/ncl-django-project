from django.views import View
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView

from django.http import JsonResponse
import json

from apps.home.models import Lesson, Student, Subscription
from apps.lessons.forms import EventForm
from django.urls import reverse_lazy

from django.contrib import messages

class Lesson_ListView(ListView):
    model = Lesson
    template_name = 'home/lesson_list.html'
    context_object_name = 'lessons'

class Lesson_CreateView(CreateView):
    model = Lesson
    form_class = EventForm
    template_name = 'forms/lesson_form.html'
    success_url = '/lessons/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cancel_url'] = reverse_lazy('lesson-list')
        return context
    
    def form_valid(self, form):
        response = super().form_valid(form)

        messages.success(self.request, 'Clase registrada exitosamente')
        return response

class Lesson_UpdateView(UpdateView):
    model = Lesson
    form_class = EventForm
    template_name = 'forms/lesson_form.html'  
    success_url = '/lessons/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cancel_url'] = reverse_lazy('lesson-list')
        return context
    
    def form_valid(self, form):
        response = super().form_valid(form)

        messages.success(self.request, 'Datos de la clase actualizados exitosamente')
        return response


def load_subscriptions(request, student_id):
    student = Student.objects.get(pk=student_id)
    subscriptions = Subscription.objects.filter(student=student)

    # data = {
    #     'id_student': student.pk,'
    #     'subscriptions': [{'id_student': sub.student.pk, 'student_name': sub.student.first_name, 'sub_id': sub.pk,'name': sub.subscription_type.name} for sub in subscriptions]
    # }
    data = {
    'student': {
        'id': student.pk,
        'name': student.first_name,
        'subscriptions': [
            {
                'id': sub.pk,
                'name': sub.subscription_type.name,
                'student': sub.student.first_name,
            }
            for sub in subscriptions
        ]
    }
}

    return JsonResponse(data)
