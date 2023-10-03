from django import forms
from .models import Student
from .models import StudentXDetail

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['first_name', 'second_name', 'first_surname', 'second_surname', 'email', 'phone_number', 'address', 'birthdate', 'is_active']
        labels = {
            'first_name': 'Primer Nombre',
            'second_name': 'Segundo Nombre',
            'first_surname': 'Primer Apellido',
            'second_surname': 'Segundo Apellido',
            'email': 'Correo Electrónico',
            'phone_number': 'Número de Teléfono',
            'address': 'Dirección',
            'birthdate': 'Fecha de Nacimiento',
            'is_active': 'Estado'
        }

    def __init__(self, *args, **kwargs):
        super(StudentForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs.update({'class': 'block py-2.5 px-0 w-full text-sm text-gray-900 bg-transparent border-0 border-b-2 border-gray-300 appearance-none dark:text-white dark:border-gray-600 dark:focus:border-blue-500 focus:outline-none focus:ring-0 focus:border-blue-600 peer', 'placeholder': ' '})
        self.fields['second_name'].widget.attrs.update({'class': 'block py-2.5 px-0 w-full text-sm text-gray-900 bg-transparent border-0 border-b-2 border-gray-300 appearance-none dark:text-white dark:border-gray-600 dark:focus:border-blue-500 focus:outline-none focus:ring-0 focus:border-blue-600 peer', 'placeholder': ' '})
        self.fields['first_surname'].widget.attrs.update({'class': 'block py-2.5 px-0 w-full text-sm text-gray-900 bg-transparent border-0 border-b-2 border-gray-300 appearance-none dark:text-white dark:border-gray-600 dark:focus:border-blue-500 focus:outline-none focus:ring-0 focus:border-blue-600 peer', 'placeholder': ' '})
        self.fields['second_surname'].widget.attrs.update({'class': 'block py-2.5 px-0 w-full text-sm text-gray-900 bg-transparent border-0 border-b-2 border-gray-300 appearance-none dark:text-white dark:border-gray-600 dark:focus:border-blue-500 focus:outline-none focus:ring-0 focus:border-blue-600 peer', 'placeholder': ' '})
        self.fields['email'].widget.attrs.update({'class': 'block py-2.5 px-0 w-full text-sm text-gray-900 bg-transparent border-0 border-b-2 border-gray-300 appearance-none dark:text-white dark:border-gray-600 dark:focus:border-blue-500 focus:outline-none focus:ring-0 focus:border-blue-600 peer', 'placeholder': ' '})
        self.fields['phone_number'].widget.attrs.update({'class': 'block py-2.5 px-0 w-full text-sm text-gray-900 bg-transparent border-0 border-b-2 border-gray-300 appearance-none dark:text-white dark:border-gray-600 dark:focus:border-blue-500 focus:outline-none focus:ring-0 focus:border-blue-600 peer', 'placeholder': ' '})
        self.fields['address'].widget.attrs.update({'class': 'block py-2.5 px-0 w-full text-sm text-gray-900 bg-transparent border-0 border-b-2 border-gray-300 appearance-none dark:text-white dark:border-gray-600 dark:focus:border-blue-500 focus:outline-none focus:ring-0 focus:border-blue-600 peer', 'placeholder': ' '})
        self.fields['birthdate'].widget.attrs.update({'class': 'block py-2.5 px-0 w-full text-sm text-gray-900 bg-transparent border-0 border-b-2 border-gray-300 appearance-none dark:text-white dark:border-gray-600 dark:focus:border-blue-500 focus:outline-none focus:ring-0 focus:border-blue-600 peer', 'placeholder': ' ', 'datepicker': '', 'datepicker-orientation': 'bottom left', 'type': 'text', 'autocomplete': 'off'})
        
        # # Agregar clases de Tailwind CSS a los widgets de los campos
        # self.fields['first_name'].widget.attrs['class'] = 'block py-2.5 px-0 w-full text-sm text-gray-900 bg-transparent border-0 border-b-2 border-gray-300 appearance-none dark:text-white dark:border-gray-600 dark:focus:border-blue-500 focus:outline-none focus:ring-0 focus:border-blue-600 peer'
        # # self.fields['first_name'].label = 'Nombre' 

        # self.fields['email'].widget.attrs['class'] = 'bg-blue-100 rounded-lg p-2'
        # self.fields['phone_number'].widget.attrs['class'] = 'bg-blue-100 rounded-lg p-2'
        # self.fields['address'].widget.attrs['class'] = 'bg-blue-100 rounded-lg p-2'
        # self.fields['birthdate'].widget.attrs['class'] = 'bg-blue-100 rounded-lg p-2'

class EventCreateForm(forms.ModelForm):
    class Meta:
        model = StudentXDetail
        fields = ['student','description', 'student_status', 'lesson_x_detail', 'start_date', 'end_date', 'subscription']

        widgets = {
        'start_date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        'end_date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
    }
