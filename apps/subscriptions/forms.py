from django import forms
from apps.home.models import Subscription

class SubscriptionForm(forms.ModelForm):
    class Meta:
        model = Subscription
        fields = ['subscription_type', 'student', 'start_date', 'end_date', 'is_active', 'auto_renewal']
        labels = {
            'subscription_type': 'Tipo de suscripción',
            'student': 'Estudiante',
            'start_date': 'Fecha nicio',
            'end_date': 'Fecha fin',
            'is_active': 'Suscripción activa',
            'auto_renewal': 'Renovación automática'
        }
        widgets = {
            'start_date':  forms.DateInput(format=('%Y-%m-%d'), attrs={'type': 'date'}),
            'end_date':  forms.DateInput(format=('%Y-%m-%d'), attrs={'type': 'date'})
        }

    def __init__(self, *args, **kwargs):
        super(SubscriptionForm, self).__init__(*args, **kwargs)

        self.fields['subscription_type'].empty_label = 'Seleccionar tipo de suscripción'
        self.fields['subscription_type'].widget.attrs.update({'class': 'block py-2.5 px-0 w-full text-sm text-gray-500 bg-transparent border-0 border-b-2 border-gray-200 appearance-none dark:text-gray-400 dark:border-gray-700 focus:outline-none focus:ring-0 focus:border-gray-200 peer'})

        self.fields['student'].empty_label = 'Seleccionar estudiante asociado'
        self.fields['student'].widget.attrs.update({'class': 'block py-2.5 px-0 w-full text-sm text-gray-500 bg-transparent border-0 border-b-2 border-gray-200 appearance-none dark:text-gray-400 dark:border-gray-700 focus:outline-none focus:ring-0 focus:border-gray-200 peer'})


        self.fields['start_date'].widget.attrs.update({'class': 'block py-2.5 px-0 w-full text-sm text-gray-500 bg-transparent border-0 border-b-2 border-gray-200 appearance-none dark:text-gray-400 dark:border-gray-700 focus:outline-none focus:ring-0 focus:border-gray-200 peer', 'placeholder': ' '})
        self.fields['end_date'].widget.attrs.update({'class': 'block py-2.5 px-0 w-full text-sm text-gray-500 bg-transparent border-0 border-b-2 border-gray-200 appearance-none dark:text-gray-400 dark:border-gray-700 focus:outline-none focus:ring-0 focus:border-gray-200 peer', 'placeholder': ' '})

        self.fields['is_active'].widget.attrs.update({'class': 'w-4 h-4 text-blue-600 bg-gray-100 border-gray-300 rounded focus:ring-blue-500 dark:focus:ring-blue-600 dark:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600'})
        self.fields['auto_renewal'].widget.attrs.update({'class': 'w-4 h-4 text-blue-600 bg-gray-100 border-gray-300 rounded focus:ring-blue-500 dark:focus:ring-blue-600 dark:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600'})

