from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView


from home.models import SubscriptionType
from home.forms import SubscriptionTypeForm

class SubscriptionTypes_ListView(ListView):
    model = SubscriptionType
    template_name = 'home/subscription_types_list.html'
    context_object_name = 'subscription_types'

class SubscriptionTypes_CreateView(CreateView):
    model = SubscriptionType
    form_class = SubscriptionTypeForm
    template_name = 'forms/subscription_types_form.html'
    success_url = '/subscription-types/'

class SubscriptionTypes_UpdateView(UpdateView):
    model = SubscriptionType
    form_class = SubscriptionTypeForm
    template_name = 'forms/subscription_types_form.html'  
    success_url = '/subscription-types/'


