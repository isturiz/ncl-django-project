
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView

from home.models import Student
from home.forms.student import StudentForm

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