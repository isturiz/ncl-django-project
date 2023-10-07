from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Student, Teacher, Lesson, TeacherXLesson, Subscription, StudentXLessonXSubscription, Payment, Renew



admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(Lesson)
admin.site.register(TeacherXLesson)

admin.site.register(Subscription)
admin.site.register(StudentXLessonXSubscription)
admin.site.register(Renew)
admin.site.register(Payment)

