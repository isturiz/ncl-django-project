from django import forms
from home.models import Lesson, Student

class EventForm(forms.ModelForm):

    student = forms.ModelChoiceField(
        queryset=Student.objects.all(),
        label='Estudiante',
        empty_label='Seleccionar estudiante'  # Opcional, agrega un texto para la opción vacía
    )
    class Meta:
        model = Lesson
        fields = ['student','lesson_type', 'subscription', 'teacher', 'description', 'price', 'start_date', 'end_date', 'lesson_status']
        labels = {
            'student': 'Estudiante',
            'lesson_type': 'Tipo de clase',
            'subscription': 'Suscripción',
            'teacher': 'Profesor',
            'description': 'Descripción',
            'price': 'Precio',
            'start_date': 'Inicio',
            'end_date': 'Fin',
            'lesson_status': 'Clase vista',
        }
        widgets = {
            'start_date':  forms.DateTimeInput(format=('%Y-%m-%dT%H:%M'), attrs={'type': 'datetime-local'}),    
            'end_date':  forms.DateTimeInput(format=('%Y-%m-%dT%H:%M'), attrs={'type': 'datetime-local'})
        }

    def __init__(self, *args, **kwargs):
        super(EventForm, self).__init__(*args, **kwargs)


        self.fields['student'].empty_label = 'Seleccionar estudiante'
        self.fields['student'].widget.attrs.update({'class': 'block py-2.5 px-0 w-full text-sm text-gray-500 bg-transparent border-0 border-b-2 border-gray-200 appearance-none dark:text-gray-400 dark:border-gray-700 focus:outline-none focus:ring-0 focus:border-gray-200 peer'})


        self.fields['lesson_type'].empty_label = 'Seleccionar tipo de clase'
        self.fields['lesson_type'].widget.attrs.update({'class': 'block py-2.5 px-0 w-full text-sm text-gray-500 bg-transparent border-0 border-b-2 border-gray-200 appearance-none dark:text-gray-400 dark:border-gray-700 focus:outline-none focus:ring-0 focus:border-gray-200 peer'})

        self.fields['subscription'].label_from_instance = lambda obj: obj.get_student_and_type()
        self.fields['subscription'].empty_label = 'Seleccionar suscripción'
        self.fields['subscription'].widget.attrs.update({'class': 'block py-2.5 px-0 w-full text-sm text-gray-500 bg-transparent border-0 border-b-2 border-gray-200 appearance-none dark:text-gray-400 dark:border-gray-700 focus:outline-none focus:ring-0 focus:border-gray-200 peer'})

        self.fields['teacher'].empty_label = 'Seleccionar profesor'
        self.fields['teacher'].widget.attrs.update({'class': 'block py-2.5 px-0 w-full text-sm text-gray-500 bg-transparent border-0 border-b-2 border-gray-200 appearance-none dark:text-gray-400 dark:border-gray-700 focus:outline-none focus:ring-0 focus:border-gray-200 peer'})

        self.fields['description'].widget.attrs.update({'class': 'block py-2.5 px-0 w-full text-sm text-gray-900 bg-transparent border-0 border-b-2 border-gray-300 appearance-none dark:text-white dark:border-gray-600 dark:focus:border-blue-500 focus:outline-none focus:ring-0 focus:border-blue-600 peer', 'placeholder': ' '})
        self.fields['price'].widget.attrs.update({'class': 'block py-2.5 px-0 w-full text-sm text-gray-900 bg-transparent border-0 border-b-2 border-gray-300 appearance-none dark:text-white dark:border-gray-600 dark:focus:border-blue-500 focus:outline-none focus:ring-0 focus:border-blue-600 peer', 'placeholder': ' ', 'step': 'any'})

        self.fields['start_date'].widget.attrs.update({'class': 'block py-2.5 px-0 w-full text-sm text-gray-500 bg-transparent border-0 border-b-2 border-gray-200 appearance-none dark:text-gray-400 dark:border-gray-700 focus:outline-none focus:ring-0 focus:border-gray-200 peer', 'placeholder': ' '})
        self.fields['end_date'].widget.attrs.update({'class': 'block py-2.5 px-0 w-full text-sm text-gray-500 bg-transparent border-0 border-b-2 border-gray-200 appearance-none dark:text-gray-400 dark:border-gray-700 focus:outline-none focus:ring-0 focus:border-gray-200 peer', 'placeholder': ' '})
        self.fields['lesson_status'].widget.attrs.update({'class': 'w-4 h-4 text-blue-600 bg-gray-100 border-gray-300 rounded focus:ring-blue-500 dark:focus:ring-blue-600 dark:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600'})

        # Verifica si ya hay un estudiante relacionado
        if self.instance.subscription_id:
            if self.instance.subscription.student:
                # Precarga el estudiante relacionado
                self.fields['student'].initial = self.instance.subscription.student

        self.fields['subscription'].disabled = True
        # self.fields['subscription'].queryset = Subscription.objects.none()


   