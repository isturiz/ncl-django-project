from django import forms
from .models import Student
from .models import StudentXDetail

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['first_name', 'email', 'phone_number', 'address', 'birthdate']

class EventCreateForm(forms.ModelForm):
    class Meta:
        model = StudentXDetail
        fields = ['student','description', 'student_status', 'lesson_x_detail', 'start_date', 'end_date', 'subscription']

        widgets = {
        'start_date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        'end_date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
    }
        