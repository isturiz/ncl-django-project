from django import forms

from home.models import Student

class StudentForm(forms.ModelForm):

    IDENTIFY_CARD_CHOICES = (
        ('V', 'Venezolano (V)'),
        ('E', 'Extranjero (E)'),
    )

    # # Crear el campo 'identify_card' como un ChoiceField
    # identify_card = forms.ChoiceField(
    #     label='Identificación',
    #     choices=IDENTIFY_CARD_CHOICES,
    # )

    identify_card_prefix = forms.ChoiceField(
        choices=IDENTIFY_CARD_CHOICES,
        label='Prefijo' 
    )
    identify_card_number = forms.CharField(max_length=19, label='Número de Identificación')

        

    class Meta:
        model = Student
        fields = ['identify_card','first_name', 'second_name', 'first_surname', 'second_surname', 'email', 'phone_number', 'address', 'birthdate', 'is_active']
        labels = {
            'first_name': 'Primer Nombre',
            'second_name': 'Segundo Nombre',
            'first_surname': 'Primer Apellido',
            'second_surname': 'Segundo Apellido',
            'email': 'Correo Electrónico',
            'phone_number': 'Número de Teléfono',
            'address': 'Dirección',
            'birthdate': 'Fecha de Nacimiento',
            'is_active': 'Estudiante activo',
            'identify_card_number': 'Número',
        }

    def __init__(self, *args, **kwargs):
        super(StudentForm, self).__init__(*args, **kwargs)
        self.fields['identify_card'].widget.attrs.update({'class': 'block py-2.5 px-0 w-full text-sm text-gray-900 bg-transparent border-0 border-b-2 border-gray-300 appearance-none dark:text-white dark:border-gray-600 dark:focus:border-blue-500 focus:outline-none focus:ring-0 focus:border-blue-600 peer', 'placeholder': ' '})
        self.fields['first_name'].widget.attrs.update({'class': 'block py-2.5 px-0 w-full text-sm text-gray-900 bg-transparent border-0 border-b-2 border-gray-300 appearance-none dark:text-white dark:border-gray-600 dark:focus:border-blue-500 focus:outline-none focus:ring-0 focus:border-blue-600 peer', 'placeholder': ' '})
        self.fields['second_name'].widget.attrs.update({'class': 'block py-2.5 px-0 w-full text-sm text-gray-900 bg-transparent border-0 border-b-2 border-gray-300 appearance-none dark:text-white dark:border-gray-600 dark:focus:border-blue-500 focus:outline-none focus:ring-0 focus:border-blue-600 peer', 'placeholder': ' '})
        self.fields['first_surname'].widget.attrs.update({'class': 'block py-2.5 px-0 w-full text-sm text-gray-900 bg-transparent border-0 border-b-2 border-gray-300 appearance-none dark:text-white dark:border-gray-600 dark:focus:border-blue-500 focus:outline-none focus:ring-0 focus:border-blue-600 peer', 'placeholder': ' '})
        self.fields['second_surname'].widget.attrs.update({'class': 'block py-2.5 px-0 w-full text-sm text-gray-900 bg-transparent border-0 border-b-2 border-gray-300 appearance-none dark:text-white dark:border-gray-600 dark:focus:border-blue-500 focus:outline-none focus:ring-0 focus:border-blue-600 peer', 'placeholder': ' '})
        self.fields['email'].widget.attrs.update({'class': 'block py-2.5 px-0 w-full text-sm text-gray-900 bg-transparent border-0 border-b-2 border-gray-300 appearance-none dark:text-white dark:border-gray-600 dark:focus:border-blue-500 focus:outline-none focus:ring-0 focus:border-blue-600 peer', 'placeholder': ' '})
        self.fields['phone_number'].widget.attrs.update({'class': 'block py-2.5 px-0 w-full text-sm text-gray-900 bg-transparent border-0 border-b-2 border-gray-300 appearance-none dark:text-white dark:border-gray-600 dark:focus:border-blue-500 focus:outline-none focus:ring-0 focus:border-blue-600 peer', 'placeholder': ' ', 'data-validate-only-numbers': 'true'})
        self.fields['address'].widget.attrs.update({'class': 'block py-2.5 px-0 w-full text-sm text-gray-900 bg-transparent border-0 border-b-2 border-gray-300 appearance-none dark:text-white dark:border-gray-600 dark:focus:border-blue-500 focus:outline-none focus:ring-0 focus:border-blue-600 peer', 'rows': '1', 'placeholder': ' '})
        self.fields['birthdate'].widget.attrs.update({'class': 'block py-2.5 px-0 w-full text-sm text-gray-900 bg-transparent border-0 border-b-2 border-gray-300 appearance-none dark:text-white dark:border-gray-600 dark:focus:border-blue-500 focus:outline-none focus:ring-0 focus:border-blue-600 peer', 'placeholder': ' ', 'datepicker': '', 'datepicker-orientation': 'bottom left', 'datepicker-format': 'dd/mm/yyyy', 'type': 'text', 'autocomplete': 'off', 'data-validate-only-dates': 'true'})
        self.fields['is_active'].widget.attrs.update({'class': 'w-4 h-4 text-blue-600 bg-gray-100 border-gray-300 rounded focus:ring-blue-500 dark:focus:ring-blue-600 dark:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600'})


        self.fields['identify_card_prefix'].empty_label = 'Seleccionar nacionalidad'
        self.fields['identify_card_prefix'].widget.attrs.update({'class': 'block py-2.5 px-0 w-full text-sm text-gray-500 bg-transparent border-0 border-b-2 border-gray-200 appearance-none dark:text-gray-400 dark:border-gray-700 focus:outline-none focus:ring-0 focus:border-gray-200 peer'})

        self.fields['identify_card_number'].widget.attrs.update({'class': 'block py-2.5 px-0 w-full text-sm text-gray-900 bg-transparent border-0 border-b-2 border-gray-300 appearance-none dark:text-white dark:border-gray-600 dark:focus:border-blue-500 focus:outline-none focus:ring-0 focus:border-blue-600 peer', 'placeholder': ' ', 'data-validate-only-numbers': 'true'})


    def clean(self):
        cleaned_data = super().clean()
        prefix = cleaned_data.get('identify_card_prefix')
        number = cleaned_data.get('identify_card_number')
        if not number.isdigit():
            self.add_error('identify_card_number', 'El número de identificación debe contener solo dígitos')

    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.identify_card = f"{self.cleaned_data['identify_card_prefix']}{self.cleaned_data['identify_card_number']}"
        if commit:
            instance.save()
        return instance
    