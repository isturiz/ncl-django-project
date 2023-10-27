from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView

from home.models import Payment
from home.forms import PaymentForm

from django.contrib import messages

class Payment_ListView(ListView):
    model = Payment
    template_name = 'home/payment_list.html'
    context_object_name = 'payments'

class Payment_CreateView(CreateView):
    model = Payment
    form_class = PaymentForm
    template_name = 'forms/payment_form.html'
    success_url = '/payments/'

    def form_valid(self, form):
        response = super().form_valid(form)

        messages.success(self.request, 'Pago registrado exitosamente')
        return response

class Payment_UpdateView(UpdateView):
    model = Payment
    form_class = PaymentForm
    template_name = 'forms/payment_form.html'  
    success_url = '/payments/'

    def form_valid(self, form):
        response = super().form_valid(form)

        messages.success(self.request, 'Datos del pago actualizados exitosamente')
        return response