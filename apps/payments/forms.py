from django import forms
from apps.home.models import Payment, Subscription

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
            # 'date':  forms.DateInput(format=('%Y-%m-%d'), attrs={'type': 'date'}),
            'date':  forms.DateTimeInput(format=('%Y-%m-%dT%H:%M'), attrs={'type': 'datetime-local'}),    

        }

    def __init__(self, *args, **kwargs):
        super(PaymentForm, self).__init__(*args, **kwargs)

        if self.instance.id is not None:
            # Si se está modificando un pago, cargar todas las suscripciones
            self.fields['subscription'].queryset = Subscription.objects.all()
        else:
            # Si se está creando un nuevo pago, cargar solo las suscripciones sin un pago asociado
            self.fields['subscription'].queryset = self.get_available_subscriptions()

        self.fields['subscription'].empty_label = 'Seleccionar suscripción'
        self.fields['subscription'].widget.attrs.update({'class': 'block py-2.5 px-0 w-full text-sm text-gray-500 bg-transparent border-0 border-b-2 border-gray-200 appearance-none dark:text-gray-400 dark:border-gray-700 focus:outline-none focus:ring-0 focus:border-gray-200 peer'})

        self.fields['price'].widget.attrs.update({'class': 'block py-2.5 px-0 w-full text-sm text-gray-900 bg-transparent border-0 border-b-2 border-gray-300 appearance-none dark:text-white dark:border-gray-600 dark:focus:border-blue-500 focus:outline-none focus:ring-0 focus:border-blue-600 peer', 'placeholder': ' '})

        self.fields['date'].widget.attrs.update({'class': 'block py-2.5 px-0 w-full text-sm text-gray-500 bg-transparent border-0 border-b-2 border-gray-200 appearance-none dark:text-gray-400 dark:border-gray-700 focus:outline-none focus:ring-0 focus:border-gray-200 peer', 'placeholder': ' '})

    def get_available_subscriptions(self):
        # Obtiene una lista de suscripciones que no tienen un pago asociado
        existing_payments = Payment.objects.values_list('subscription_id', flat=True)
        return Subscription.objects.exclude(id__in=existing_payments)