from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Student
from .models import Educator
from .models import Lesson


admin.site.register(Student)
admin.site.register(Educator)
admin.site.register(Lesson)
