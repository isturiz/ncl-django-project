from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView

from home.models import Subscription
from home.forms import SubscriptionForm

from django.contrib import messages


class SubscriptionListView(ListView):
    model = Subscription
    template_name = 'home/subscription_list.html'
    context_object_name = 'subscriptions'

class SubscriptionCreateView(CreateView):
    model = Subscription
    form_class = SubscriptionForm
    template_name = 'forms/subscription_form.html'
    success_url = '/subscriptions/'

    def form_valid(self, form):
        response = super().form_valid(form)

        messages.success(self.request, 'Suscripción creada exitosamente')
        return response

class SubscriptionUpdateView(UpdateView):
    model = Subscription
    form_class = SubscriptionForm
    template_name = 'forms/subscription_form.html'  
    success_url = '/subscriptions/'

    def form_valid(self, form):
        response = super().form_valid(form)

        messages.success(self.request, 'Datos de la suscripción actualizados exitosamente')
        return response

