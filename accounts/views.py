from django.shortcuts import render
from django.http import HttpResponse

from django.views.generic import TemplateView

# Create your views here.
from .forms import CustomLoginForm

def login_view(request):
    if request.method == 'POST':
        form = CustomLoginForm(request.POST)
        if form.is_valid():
            pass
    else:
        form = CustomLoginForm()

    return render(request, 'login.html', {'form': form})