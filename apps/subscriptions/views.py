from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView

from apps.home.models import Subscription
from apps.subscriptions.forms import SubscriptionForm

from django.contrib import messages


class Subscription_ListView(ListView):
    model = Subscription
    template_name = 'home/subscription_list.html'
    context_object_name = 'subscriptions'

class Subscription_CreateView(CreateView):
    model = Subscription
    form_class = SubscriptionForm
    template_name = 'forms/subscription_form.html'
    success_url = '/subscriptions/'

    def form_valid(self, form):
        response = super().form_valid(form)

        messages.success(self.request, 'Suscripción creada exitosamente')
        return response

class Subscription_UpdateView(UpdateView):
    model = Subscription
    form_class = SubscriptionForm
    template_name = 'forms/subscription_form.html'  
    success_url = '/subscriptions/'

    def form_valid(self, form):
        response = super().form_valid(form)

        messages.success(self.request, 'Datos de la suscripción actualizados exitosamente')
        return response

