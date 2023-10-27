from django.shortcuts import render
from django.http import HttpResponse

from django.views.generic import TemplateView

# Create your views here.
from accounts.forms import CustomLoginForm, CustomUserChangeForm

from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy
from accounts.forms import CustomRegistrationForm
from django.contrib.auth import login
from django.contrib.auth.models import User 

from django.contrib import messages


def login_view(request):
    if request.method == 'POST':
        form = CustomLoginForm(request.POST)
        if form.is_valid():
            pass
    else:
        form = CustomLoginForm()

    return render(request, 'login.html', {'form': form})

class UserCreateView(CreateView):
    model = User
    template_name = 'registration/register_user.html'
    form_class = CustomRegistrationForm
    success_url = reverse_lazy('user-list')

    def form_valid(self, form):
        response = super().form_valid(form)

        messages.success(self.request, 'Usuario creado exitosamente')
        return response

class UserUpdateView(UpdateView):
    model = User
    form_class = CustomUserChangeForm  # Usa tu formulario personalizado para la edición
    template_name = 'registration/edit_user.html'  # Crea una plantilla para la edición de usuarios
    success_url = reverse_lazy('user-list') 

    def form_valid(self, form):
        response = super().form_valid(form)

        messages.success(self.request, 'Usuario actualizado exitosamente')
        return response