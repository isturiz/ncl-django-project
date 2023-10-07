from django import forms
from .models import Student
from .models import StudentXLessonXSubscription

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
            'is_active': 'Estudiante activo'
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
        self.fields['is_active'].widget.attrs.update({'class': 'w-4 h-4 text-blue-600 bg-gray-100 border-gray-300 rounded focus:ring-blue-500 dark:focus:ring-blue-600 dark:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600'})


class EventCreateForm(forms.ModelForm):
    class Meta:
        model = StudentXLessonXSubscription
        fields = ['student','description', 'student_status', 'lesson', 'start_date', 'end_date', 'subscription']
        labels = {
            'student': 'Estudiante',
            'description': 'Descripción',
            'student_status': 'Estatus del estudiante',
            'lesson': 'IDK',
            'start_date': 'Inicio',
            'end_date': 'Fin',
            'subscription': 'Suscripción',
        }
        widgets = {
            'start_date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'end_date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }

    def __init__(self, *args, **kwargs):
        super(EventCreateForm, self).__init__(*args, **kwargs)
        self.fields['student'].empty_label = 'Selecciona un estudiante'
        self.fields['student'].widget.attrs.update({'class': 'block py-2.5 px-0 w-full text-sm text-gray-500 bg-transparent border-0 border-b-2 border-gray-200 appearance-none dark:text-gray-400 dark:border-gray-700 focus:outline-none focus:ring-0 focus:border-gray-200 peer'})

        self.fields['description'].widget.attrs.update({'class': 'block py-2.5 px-0 w-full text-sm text-gray-900 bg-transparent border-0 border-b-2 border-gray-300 appearance-none dark:text-white dark:border-gray-600 dark:focus:border-blue-500 focus:outline-none focus:ring-0 focus:border-blue-600 peer', 'placeholder': ' '})
        self.fields['student_status'].widget.attrs.update({'class': 'block py-2.5 px-0 w-full text-sm text-gray-900 bg-transparent border-0 border-b-2 border-gray-300 appearance-none dark:text-white dark:border-gray-600 dark:focus:border-blue-500 focus:outline-none focus:ring-0 focus:border-blue-600 peer', 'placeholder': ' '})

        self.fields['lesson'].empty_label = 'Selecciona'
        self.fields['lesson'].widget.attrs.update({'class': 'block py-2.5 px-0 w-full text-sm text-gray-500 bg-transparent border-0 border-b-2 border-gray-200 appearance-none dark:text-gray-400 dark:border-gray-700 focus:outline-none focus:ring-0 focus:border-gray-200 peer'})

        self.fields['subscription'].widget.attrs.update({'class': 'block py-2.5 px-0 w-full text-sm text-gray-500 bg-transparent border-0 border-b-2 border-gray-200 appearance-none dark:text-gray-400 dark:border-gray-700 focus:outline-none focus:ring-0 focus:border-gray-200 peer'})
        # self.fields['lesson_x_detail'].widget.attrs.update({'class': 'block py-2.5 px-0 w-full text-sm text-gray-900 bg-transparent border-0 border-b-2 border-gray-300 appearance-none dark:text-white dark:border-gray-600 dark:focus:border-blue-500 focus:outline-none focus:ring-0 focus:border-blue-600 peer', 'placeholder': ' '})
        # self.fields['start_date'].widget.attrs.update({'class': 'block py-2.5 px-0 w-full text-sm text-gray-900 bg-transparent border-0 border-b-2 border-gray-300 appearance-none dark:text-white dark:border-gray-600 dark:focus:border-blue-500 focus:outline-none focus:ring-0 focus:border-blue-600 peer', 'placeholder': ' '})
        # self.fields['end_date'].widget.attrs.update({'class': 'block py-2.5 px-0 w-full text-sm text-gray-900 bg-transparent border-0 border-b-2 border-gray-300 appearance-none dark:text-white dark:border-gray-600 dark:focus:border-blue-500 focus:outline-none focus:ring-0 focus:border-blue-600 peer', 'placeholder': ' '})
        # self.fields['subscription'].widget.attrs.update({'class': 'block py-2.5 px-0 w-full text-sm text-gray-900 bg-transparent border-0 border-b-2 border-gray-300 appearance-none dark:text-white dark:border-gray-600 dark:focus:border-blue-500 focus:outline-none focus:ring-0 focus:border-blue-600 peer', 'placeholder': ' '})
        # self.fields['birthdate'].widget.attrs.update({'class': 'block py-2.5 px-0 w-full text-sm text-gray-900 bg-transparent border-0 border-b-2 border-gray-300 appearance-none dark:text-white dark:border-gray-600 dark:focus:border-blue-500 focus:outline-none focus:ring-0 focus:border-blue-600 peer', 'placeholder': ' ', 'datepicker': '', 'datepicker-orientation': 'bottom left', 'type': 'text', 'autocomplete': 'off'})
        # self.fields['is_active'].widget.attrs.update({'class': 'w-4 h-4 text-blue-600 bg-gray-100 border-gray-300 rounded focus:ring-blue-500 dark:focus:ring-blue-600 dark:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600'})
