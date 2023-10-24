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
    print('-------------------------', student_id)
    student = Student.objects.get(pk=student_id)
    # subscriptions = student.subscription_set.all()  # Asume que el modelo de Student tiene una relación con Subscription

    # subscriptions = Subscription.objects.filter()
    subscriptions = Subscription.objects.filter(student=student)
    print(subscriptions)

    data = {
        'subscriptions': [{'id': sub.student.pk, 'student_name': sub.student.first_name, 'sub_id': sub.pk,'name': sub.subscription_type.name} for sub in subscriptions]
    }

    return JsonResponse(data)

class LoadSubscription_View(View):
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