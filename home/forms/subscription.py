from django import forms
from home.models import Subscription

class SubscriptionForm(forms.ModelForm):
    class Meta:
        model = Subscription
        fields = ['subscription_type', 'student', 'start_date', 'end_date', 'is_active']
        labels = {
            'subscription_type': 'Tipo de suscripción',
            'student': 'Estudiante',
            'start_date': 'Fecha nicio',
            'end_date': 'Fecha fin',
            'is_active': 'Suscripción activa',
        }
        widgets = {
            'start_date':  forms.DateInput(format=('%Y-%m-%d'), attrs={'type': 'date'}),
            'end_date':  forms.DateInput(format=('%Y-%m-%d'), attrs={'type': 'date'})
        }