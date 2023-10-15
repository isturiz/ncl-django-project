from django.contrib import admin
from .models import SubscriptionType, LessonType, Lesson, Teacher, Payment, LessonXSubscriptionXTeacher, SubscriptionXStudentXPayment, Student, Subscription

# Guide
# search_fields = () <- Search fields for the admin interface
# list_display = () <- List of fields to display in the admin interface
# list_filter = () <- List of fields to filter the results by
# list_per_page = () <- Number of results to display per page
# ordering = () <- Ordering of the results


# class SubscriptionInline(admin.TabularInline):
#     model = Student.subscriptions.through  # Accede a la tabla intermedia
#     extra = 1  # Número de registros en blanco para agregar

# class StudentAdmin(admin.ModelAdmin):
#     inlines = [SubscriptionInline]

# admin.site.register(Student, StudentAdmin)




# class StudentInline(admin.TabularInline):
#     model = Subscription.students.through  # Accede a la tabla intermedia
#     extra = 1  # Número de registros en blanco para agregar

# class SubscriptionAdmin(admin.ModelAdmin):
#     inlines = [StudentInline]

# admin.site.register(Subscription, SubscriptionAdmin)



# Define admin classes for your models

# class LessonAdmin(admin.ModelAdmin):
#     filter_horizontal = ('subscriptions',)

# class SubscriptionAdmin(admin.ModelAdmin):
#     filter_horizontal = ('students', 'lessons')

# class LessonXSubscriptionAdmin(admin.ModelAdmin):
#     list_display = ('lesson', 'subscription', 'teacher')

# class SubscriptionXStudentXPaymentAdmin(admin.ModelAdmin):
#     list_display = ('subscription', 'student', 'payment')


class LessonXSubscriptionXTeacherInline(admin.TabularInline):
    model = LessonXSubscriptionXTeacher
    extra = 1 

class LessonAdmin(admin.ModelAdmin):
    inlines = [LessonXSubscriptionXTeacherInline]
    # list_display = ('lesson_type', 'price', 'start_date', 'end_date', 'lesson_status')
    # filter_horizontal = ('subscriptions',)

admin.site.register(Lesson, LessonAdmin)
admin.site.register(LessonXSubscriptionXTeacher)


class SubscriptionXStudentXPaymentInline(admin.TabularInline):
    model = SubscriptionXStudentXPayment
    extra = 1

class SubscriptionAdmin(admin.ModelAdmin):
    inlines = [SubscriptionXStudentXPaymentInline]

admin.site.register(Subscription, SubscriptionAdmin)


class PaymentAdmin(admin.ModelAdmin):
    inlines = [SubscriptionXStudentXPaymentInline]

admin.site.register(Payment, PaymentAdmin)

admin.site.register(SubscriptionType)
admin.site.register(LessonType)
admin.site.register(Teacher)
admin.site.register(Student)

admin.site.register(SubscriptionXStudentXPayment)
