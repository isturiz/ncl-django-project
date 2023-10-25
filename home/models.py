from django.db import models
from django.db.models import UniqueConstraint
from datetime import timedelta
from dateutil.relativedelta import relativedelta
from datetime import date
import calendar
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _


SUBSCRIPTION_DURATION = 30

class SubscriptionType(models.Model):

    # Fields
    name = models.CharField(verbose_name=_('Name'), max_length=255)
    description = models.TextField(verbose_name=_('Description'), blank=True, null=True)
    price = models.DecimalField(verbose_name=_('Price'), max_digits=10, decimal_places=2, blank=True, null=True)
    number_of_lessons = models.IntegerField(verbose_name=_('Number of Lessons'), blank=True, null=True)

    def __str__(self):
        return f'{self.name} - Precio: {self.price} - Número de clases: {self.number_of_lessons}'
    
    class Meta:
        constraints = [
            UniqueConstraint(
                fields=['name', 'price'],
                name='unique_subscription_type'
            )
        ]


class LessonType(models.Model):

    # Fields
    cathedra = models.CharField(verbose_name=_('Cathedra'), max_length=255)
    modality = models.CharField(verbose_name=_('Modality'), max_length=255)

    def __str__(self):
        return f'{self.cathedra} - {self.modality}'
    
    class Meta:
        constraints = [
            UniqueConstraint(fields=['cathedra', 'modality'], name='unique_lesson_type')
        ]


class Lesson(models.Model):

    # Foreign Keys
    lesson_type = models.ForeignKey(LessonType, on_delete=models.CASCADE)
    subscription = models.ForeignKey('Subscription', on_delete=models.CASCADE)
    teacher = models.ForeignKey('Teacher', on_delete=models.CASCADE)

    # Fields
    description = models.CharField(verbose_name=_('Description'), max_length=200, blank=True, null=True)
    price = models.DecimalField(verbose_name=_('Price'), max_digits=10, decimal_places=2, blank=True, null=True)
    start_date = models.DateTimeField(verbose_name=_('Start Date'), blank=True, null=True)
    end_date = models.DateTimeField(verbose_name=_('End Date'), blank=True, null=True)
    lesson_status = models.BooleanField(verbose_name=_('Lesson Status'), default=False)  # True = Vista, False = No vista


    def __str__(self):
        return f'{self.lesson_type} - {self.price} - {self.subscription}'
    
    


class Teacher(models.Model):

    # Fields
    identify_card = models.CharField(verbose_name=_('Identify Card'), max_length=20, blank=True, null=True)
    first_name = models.CharField(verbose_name=_('First Name'), max_length=255)
    second_name = models.CharField(verbose_name=_('Second Name'), max_length=255, blank=True, null=True)
    first_surname = models.CharField(verbose_name=_('First Surname'), max_length=255)
    second_surname = models.CharField(verbose_name=_('Second Surname'), max_length=255, blank=True, null=True)
    birthdate = models.DateField(verbose_name=_('Birthdate'))
    phone_number = models.CharField(verbose_name=_('Phone'), max_length=20)
    email = models.EmailField(verbose_name=_('Email'))
    address = models.TextField(verbose_name=_('Address'))
    is_active = models.BooleanField(verbose_name=_('Active'), default=True)
    
    def __str__(self):
        return f'{self.first_name} {self.first_surname}'
    
    class Meta:
        constraints = [
            UniqueConstraint(
                fields=['identify_card','first_name', 'second_name', 'first_surname', 'second_surname', 'birthdate'],
                name='unique_teacher'
            )
        ]
    

class Student(models.Model):

    # Fields
    identify_card = models.CharField(verbose_name=_('Identify Card'), max_length=20, blank=True, null=True)
    first_name = models.CharField(verbose_name=_('First Name'), max_length=255)
    second_name = models.CharField(verbose_name=_('Second Name'), max_length=255, blank=True, null=True)
    first_surname = models.CharField(verbose_name=_('First Surname'), max_length=255)
    second_surname = models.CharField(verbose_name=_('Second Surname'), max_length=255, blank=True, null=True)
    birthdate = models.DateField(verbose_name=_('Birthdate'))
    phone_number = models.CharField(verbose_name=_('Phone'), max_length=20)
    email = models.EmailField(verbose_name=_('Email'), )
    address = models.TextField(verbose_name=_('Address'), )
    is_active = models.BooleanField(verbose_name=_('Active'), default=True)


    def __str__(self):
        return f'{self.first_name} {self.first_surname}'
    
    class Meta:
        constraints = [
            UniqueConstraint(
                fields=['identify_card','first_name', 'second_name', 'first_surname', 'second_surname', 'birthdate'],
                name='unique_student'
            )
        ]


class Subscription(models.Model):

    # Foreign Keys
    subscription_type = models.ForeignKey(SubscriptionType, on_delete=models.CASCADE)
    student = models.ForeignKey('Student', on_delete=models.CASCADE)

    # Fields
    start_date = models.DateField(verbose_name=_('Start Date'))
    end_date = models.DateField(verbose_name=_('End Date'))
    is_active = models.BooleanField(verbose_name=_('Active'), default=True)
    auto_renewal = models.BooleanField(verbose_name=_('Auto Renewal'), default=True)
    

    def __str__(self):
        return f'{self.student} - {self.subscription_type}'
    
    def get_student_name(self):
        return str(self.student)
    
    def get_student_and_type (self):
        return f'{self.student} - {self.subscription_type.name} - ${self.subscription_type.price}'
    
    # If auto_renewal is True, renews the subscription
    def renew_subscription(self):
        if self.auto_renewal:
            current_month = self.end_date.month
            current_year = self.end_date.year

            # Get the last day of the new month
            if current_month == 12:
                new_month = 1
                new_year = current_year + 1
            else:
                new_month = current_month + 1
                new_year = current_year

            # Get the last day of the new month
            last_day_of_new_month = calendar.monthrange(new_year, new_month)[1]
            if self.end_date.day > last_day_of_new_month:
                new_day = last_day_of_new_month
            else:
                new_day = self.end_date.day

            # Create a new subscription
            new_subscription = Subscription(
                subscription_type = self.subscription_type,
                student = self.student,
                start_date = self.end_date,
                end_date = date(new_year, new_month, new_day),
                is_active = True,
                auto_renewal = True  
            )
            new_subscription.save()

            self.auto_renewal = False
            self.is_active = False
            self.save()


class Payment(models.Model):

    # Foreign Key
    subscription = models.ForeignKey(Subscription, on_delete=models.CASCADE, related_name='payments')

    # Fields
    price = models.DecimalField(verbose_name=_('Price'), max_digits=10, decimal_places=2)
    date = models.DateTimeField(verbose_name=_('Date'), )



    def __str__(self):
        return f'{self.price} - {self.subscription} - {self.date}'
    
class ActivityLog(models.Model):
    user = models.ForeignKey(      "auth.User",
        on_delete=models.CASCADE,
        related_name="activity_logs",
    )
    ip_address = models.GenericIPAddressField(null=True, blank=True)
    action = models.CharField(max_length=255)
    url = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} {self.action} {self.url}"
    
class ActivityLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    action = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} - {self.action}'
    
from auditlog.registry import auditlog
    
auditlog.register(SubscriptionType)
auditlog.register(LessonType)
auditlog.register(Lesson)
auditlog.register(Teacher)
auditlog.register(Student)
auditlog.register(Subscription)
auditlog.register(Payment)