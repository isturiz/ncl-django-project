from django.shortcuts import render
from django.http import HttpResponse

from django.views.generic import TemplateView

# Create your views here.
from accounts.forms import CustomLoginForm

from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from accounts.forms import CustomRegistrationForm
from django.contrib.auth import login


def login_view(request):
    if request.method == 'POST':
        form = CustomLoginForm(request.POST)
        if form.is_valid():
            pass
    else:
        form = CustomLoginForm()

    return render(request, 'login.html', {'form': form})

class UserCreateView(CreateView):
    template_name = 'registration/register.html'
    form_class = CustomRegistrationForm  # Utiliza el formulario de creación de usuarios predeterminado
    success_url = reverse_lazy('user-list')  # Redirige a la lista de usuarios u otra página

# class Student_CreateView(CreateView):
#     model = Student
#     form_class = StudentForm
#     template_name = 'forms/student_form.html'  
#     success_url = '/students/'
