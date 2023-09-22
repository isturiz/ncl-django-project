from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Student, Teacher, Lesson, LessonType, LessonXDetail, TeacherXDetail, Subscription, Payment, SubscriptionXDetail, RenewSubscription, StudentXDetail



admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(Lesson)
admin.site.register(LessonType)
admin.site.register(LessonXDetail)
admin.site.register(TeacherXDetail)
admin.site.register(Subscription)
admin.site.register(Payment)
admin.site.register(SubscriptionXDetail)
admin.site.register(RenewSubscription)
admin.site.register(StudentXDetail)
