from django import forms
from home.models import SubscriptionType

class SubscriptionTypeForm(forms.ModelForm):
    class Meta:
        model = SubscriptionType
        fields = ['name', 'description', 'price', 'number_of_lessons']
        labels = {
            'name': 'Nombre',
            'description': 'Descripción',
            'price': 'Precio',
            'number_of_lessons': 'Número de clases',
        }

    def __init__(self, *args, **kwargs):
        super(SubscriptionTypeForm, self).__init__(*args, **kwargs)

        self.fields['name'].widget.attrs.update({'class': 'block py-2.5 px-0 w-full text-sm text-gray-900 bg-transparent border-0 border-b-2 border-gray-300 appearance-none dark:text-white dark:border-gray-600 dark:focus:border-blue-500 focus:outline-none focus:ring-0 focus:border-blue-600 peer', 'placeholder': ' '})
        self.fields['description'].widget.attrs.update({'class': 'block py-2.5 px-0 w-full text-sm text-gray-900 bg-transparent border-0 border-b-2 border-gray-300 appearance-none dark:text-white dark:border-gray-600 dark:focus:border-blue-500 focus:outline-none focus:ring-0 focus:border-blue-600 peer', 'placeholder': ' ', 'rows': '1',})
        self.fields['price'].widget.attrs.update({'class': 'block py-2.5 px-0 w-full text-sm text-gray-900 bg-transparent border-0 border-b-2 border-gray-300 appearance-none dark:text-white dark:border-gray-600 dark:focus:border-blue-500 focus:outline-none focus:ring-0 focus:border-blue-600 peer', 'placeholder': ' '})
        self.fields['number_of_lessons'].widget.attrs.update({'class': 'block py-2.5 px-0 w-full text-sm text-gray-900 bg-transparent border-0 border-b-2 border-gray-300 appearance-none dark:text-white dark:border-gray-600 dark:focus:border-blue-500 focus:outline-none focus:ring-0 focus:border-blue-600 peer', 'placeholder': ' '})
