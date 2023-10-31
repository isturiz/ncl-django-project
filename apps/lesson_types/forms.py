from django import forms
from apps.home.models import LessonType

class LessonTypeForm(forms.ModelForm):
    class Meta:
        model = LessonType
        fields = ['cathedra', 'modality']
        labels = {
            'cathedra': 'Tipo de clase',
            'modality': 'Modalidad',
        }

    def __init__(self, *args, **kwargs):
        super(LessonTypeForm, self).__init__(*args, **kwargs)

        self.fields['cathedra'].widget.attrs.update({'class': 'block py-2.5 px-0 w-full text-sm text-gray-900 bg-transparent border-0 border-b-2 border-gray-300 appearance-none dark:text-white dark:border-gray-600 dark:focus:border-blue-500 focus:outline-none focus:ring-0 focus:border-blue-600 peer', 'placeholder': ' '})
        self.fields['modality'].widget.attrs.update({'class': 'block py-2.5 px-0 w-full text-sm text-gray-900 bg-transparent border-0 border-b-2 border-gray-300 appearance-none dark:text-white dark:border-gray-600 dark:focus:border-blue-500 focus:outline-none focus:ring-0 focus:border-blue-600 peer', 'placeholder': ' '})