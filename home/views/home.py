from django.views.generic import TemplateView

from home.models import Student
from home.forms import StudentForm

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