from django.contrib import admin
from .models import SubscriptionType, LessonType, Lesson, Teacher, Payment, Student, Subscription, ActivityLog
# Guide
# search_fields = () <- Search fields for the admin interface
# list_display = () <- List of fields to display in the admin interface
# list_filter = () <- List of fields to filter the results by
# list_per_page = () <- Number of results to display per page
# ordering = () <- Ordering of the results
# exclude = () <- List of fields to exclude from the admin interface

admin.site.register(Lesson)

class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ('id', 'student', 'subscription_type', 'start_date', 'end_date', 'is_active', 'auto_renewal')

admin.site.register(Subscription, SubscriptionAdmin)

class PaymentAdmin(admin.ModelAdmin):
    list_display = ('price', 'date', 'subscription')
    # list_filter = ('date',)  # Agrega filtrado por fecha en el admin

admin.site.register(Payment, PaymentAdmin)

admin.site.register(SubscriptionType)
admin.site.register(LessonType)
admin.site.register(Teacher)

class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'identify_card', 'first_name', 'second_name', 'first_surname', 'second_surname', 'birthdate', 'phone_number', 'email', 'address', 'is_active')

admin.site.register(Student, StudentAdmin)
admin.site.register(ActivityLog)
