from django import forms
from home.models import Payment

class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ['price', 'date', 'subscription']
        labels = {
            'price': 'Monto',
            'date': 'Fecha del pago',
            'subscription': 'Suscripción',
        }
        widgets = {
            'date':  forms.DateInput(format=('%Y-%m-%d'), attrs={'type': 'date'}),
        }