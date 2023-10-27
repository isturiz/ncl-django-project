from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView


from home.models import LessonType
from home.forms import LessonTypeForm

from django.contrib import messages


class LessonTypes_ListView(ListView):
    model = LessonType
    template_name = 'home/lesson_types_list.html'
    context_object_name = 'lesson_types'

class LessonTypes_CreateView(CreateView):
    model = LessonType
    form_class = LessonTypeForm
    template_name = 'forms/lesson_types_form.html'
    success_url = '/lesson-types/'

    def form_valid(self, form):
        response = super().form_valid(form)

        messages.success(self.request, 'Tipo de clase creado exitosamente')
        return response

class LessonTypes_UpdateView(UpdateView):
    model = LessonType
    form_class = LessonTypeForm
    template_name = 'forms/lesson_types_form.html'  
    success_url = '/lesson-types/'

    def form_valid(self, form):
        response = super().form_valid(form)

        messages.success(self.request, 'Datos del tipo de clase actualizados exitosamente')
        return response



