from django import forms
from home.models import Subscription

class SubscriptionForm(forms.ModelForm):
    class Meta:
        model = Subscription
        fields = ['subscription_type', 'student', 'start_date', 'end_date', 'subscription_status']
        labels = {
            'subscription_type': 'Tipo de suscripción',
            'student': 'Estudiante',
            'start_date': 'Fecha nicio',
            'end_date': 'Fecha fin',
            'subscription_status': 'Suscripción activa',
        }
        widgets = {
            'start_date':  forms.DateInput(format=('%Y-%m-%d'), attrs={'type': 'date'}),
            'end_date':  forms.DateInput(format=('%Y-%m-%d'), attrs={'type': 'date'})
        }