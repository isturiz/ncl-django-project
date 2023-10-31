from django.views import View
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView

from django.http import JsonResponse
from django.urls import reverse_lazy

from apps.home.models import Lesson
from apps.fullcalendar.forms import EventForm

from django.contrib import messages


class CalendarView(ListView):
    model = Lesson
    # model = Subscription
    template_name = 'home/calendar.html'
    context_object_name = 'events'

class EventCreateView(CreateView):
    model = Lesson
    form_class = EventForm
    template_name = 'forms/lesson_form.html'
    success_url = reverse_lazy('calendar')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cancel_url'] = reverse_lazy('calendar')
        return context
    
    def form_valid(self, form):
        response = super().form_valid(form)

        messages.success(self.request, 'Clase registrada exitosamente')
        return response


class EventLessonUpdateView(UpdateView):
    model = Lesson
    form_class = EventForm
    template_name = 'forms/lesson_form.html'  
    success_url = reverse_lazy('calendar')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cancel_url'] = reverse_lazy('calendar')
        return context
    
    def form_valid(self, form):
        response = super().form_valid(form)

        messages.success(self.request, 'Datos de la clase actualizados exitosamente')
        return response
    
        
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
