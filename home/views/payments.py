from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView

from home.models import Payment
from home.forms import PaymentForm

class PaymentListView(ListView):
    model = Payment
    template_name = 'home/payment_list.html'
    context_object_name = 'payments'

class PaymentCreateView(CreateView):
    model = Payment
    form_class = PaymentForm
    template_name = 'forms/payment_form.html'
    success_url = '/payments/'

class PaymentUpdateView(UpdateView):
    model = Payment
    form_class = PaymentForm
    template_name = 'forms/payment_form.html'  
    success_url = '/payments/'