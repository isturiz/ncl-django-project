from django.urls import reverse
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView


from apps.home.models import SubscriptionType
from apps.subscription_types.forms import SubscriptionTypeForm

from django.contrib import messages


class SubscriptionTypes_ListView(ListView):
    model = SubscriptionType
    template_name = 'home/subscription_types_list.html'
    context_object_name = 'subscription_types'

class SubscriptionTypes_CreateView(CreateView):
    model = SubscriptionType
    form_class = SubscriptionTypeForm
    template_name = 'forms/subscription_types_form.html'
    success_url = '/subscription_types/'

    def form_valid(self, form):
        response = super().form_valid(form)

        messages.success(self.request, 'Tipo de suscripción creado exitosamente')
        return response

class SubscriptionTypes_UpdateView(UpdateView):
    model = SubscriptionType
    form_class = SubscriptionTypeForm
    template_name = 'forms/subscription_types_form.html'  
    success_url = '/subscription_types/'


    def form_valid(self, form):
            response = super().form_valid(form)

            messages.success(self.request, 'Datos de tipo de suscripción actualizados exitosamente')
            return response



