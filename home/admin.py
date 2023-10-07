from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Student, Teacher, Lesson, Subscription, Payment



admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(Lesson)

admin.site.register(Subscription)
admin.site.register(Payment)

