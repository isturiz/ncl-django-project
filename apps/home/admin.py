from django.contrib import admin
from .models import SubscriptionType, LessonType, Lesson, Teacher, Payment, Student, Subscription, ActivityLog
# Guide
# search_fields = () <- Search fields for the admin interface
# list_display = () <- List of fields to display in the admin interface
# list_filter = () <- List of fields to filter the results by
# list_per_page = () <- Number of results to display per page
# ordering = () <- Ordering of the results
# exclude = () <- List of fields to exclude from the admin interface


class LessonAdmin(admin.ModelAdmin):
    list_display = ('lesson_type', 'teacher', 'subscription', 'price')
    search_fields = ['price', 'teacher__first_name', 'subscription__subscription_type__name']

admin.site.register(Lesson, LessonAdmin)

class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ('id', 'student', 'subscription_type', 'start_date', 'end_date', 'is_active', 'auto_renewal')
    search_fields = ['student__first_name', 'subscription_type__name']


admin.site.register(Subscription, SubscriptionAdmin)

class PaymentAdmin(admin.ModelAdmin):
    list_display = ('price', 'date', 'subscription')
    list_filter = ('date',) 
    search_fields = ['price', 'date', 'subscription__student__first_name', 'subscription__subscription_type__name']

    # list_filter = ('date',)  # Agrega filtrado por fecha en el admin

admin.site.register(Payment, PaymentAdmin)

class SubscriptionTypeAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'description', 'price', 'number_of_lessons')
    list_filter = ('name',) 
    search_fields = ['name', 'description', 'price', 'number_of_lessons']

    # list_filter = ('date',)  # Agrega filtrado por fecha en el admin


admin.site.register(SubscriptionType, SubscriptionTypeAdmin)
admin.site.register(LessonType)
admin.site.register(Teacher)

class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'identify_card', 'first_name', 'second_name', 'first_surname', 'second_surname', 'birthdate', 'phone_number', 'email', 'address', 'is_active')

admin.site.register(Student, StudentAdmin)
admin.site.register(ActivityLog)
