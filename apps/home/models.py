from django.db import models
from django.db.models import UniqueConstraint
from datetime import timedelta
from dateutil.relativedelta import relativedelta
from datetime import date
import calendar
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

from django.core.exceptions import ValidationError
from django.utils import timezone
from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.contrib.auth.models import BaseUserManager




class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, password, **extra_fields)

class User(AbstractUser, PermissionsMixin):
    STUDENT = 'ST'
    TEACHER = 'TC'
    DIRECTOR = 'DR'
    ADMINISTRATOR = 'AD'

    ROLE_CHOICES = [
        (STUDENT, 'Student'),
        (TEACHER, 'Teacher'),
        (DIRECTOR, 'Director'),
        (ADMINISTRATOR, 'Administrator'),
    ]
    username = models.CharField(
        max_length=254, 
        unique=True, 
        verbose_name='username'
    )
    first_name = models.CharField(
        _('first name'),
        blank=False,
        null=False,
        max_length=150,
    )
    last_name = models.CharField(
        _('last name'),
        blank=False,
        null=False,
        max_length=150,
    )
    last_login = models.DateField(
        _("last login"),
        auto_now=True,
        blank=True,
        null=True,
    )
    email = models.EmailField(_('email address'), unique=True)
    role = models.CharField(_('role'), max_length=2, choices=ROLE_CHOICES, default=STUDENT)
    is_active = models.BooleanField(_('active'), default=True)
    is_staff = models.BooleanField(_('staff status'), default=False)

    objects = CustomUserManager()

    # Agrega related_name personalizados para evitar conflictos
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name=_('user permissions'),
        blank=True,
        related_name='customuser_user_permissions'
    )
    groups = models.ManyToManyField(
        'auth.Group',
        verbose_name=_('groups'),
        blank=True,
        related_name='customuser_groups'
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email


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
    lesson_type = models.ForeignKey(LessonType, on_delete=models.CASCADE, verbose_name=_('Lesson Type'))
    subscription = models.ForeignKey('Subscription', on_delete=models.CASCADE, verbose_name=_('Subscription'))
    teacher = models.ForeignKey('Teacher', on_delete=models.CASCADE, verbose_name=_('Teacher'))

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
    identify_card = models.CharField(verbose_name=_('Identify Card'), max_length=20, blank=True, null=True, unique=True)
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

    def clean(self):
        super().clean()

        # Comprueba si ya existe un profesor con los mismos datos
        existing_teacher = Teacher.objects.filter(
            identify_card=self.identify_card,
            first_name=self.first_name,
            second_name=self.second_name,
            first_surname=self.first_surname,
            second_surname=self.second_surname,
            birthdate=self.birthdate
        ).exclude(id=self.id)

        if existing_teacher.exists():
            raise ValidationError("Ya existe un profesor registrado con esos datos.")


    

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
    subscription_type = models.ForeignKey(SubscriptionType, on_delete=models.CASCADE, verbose_name=_('Subscription Type'))
    student = models.ForeignKey('Student', on_delete=models.CASCADE, verbose_name=_('Student'))

    # Fields
    start_date = models.DateField(verbose_name=_('Start Date'))
    end_date = models.DateField(verbose_name=_('End Date'))
    is_active = models.BooleanField(verbose_name=_('Active'), default=True)
    auto_renewal = models.BooleanField(verbose_name=_('Auto Renewal'), default=True)


    def __str__(self):
        return f'{self.student} - {self.subscription_type}'
    
    def get_student_name(self):
        return str(self.student)
    
    def get_subscription_type_name(self):
        return str(self.subscription_type.name)
    
    def get_student_and_type (self):
        return f'{self.student} - {self.subscription_type.name} - ${self.subscription_type.price}'
    
    def clean(self):
        super().clean()
        
        # Comprueba si existe una suscripción activa que se superpone
        overlapping_subscriptions = Subscription.objects.filter(
            student=self.student,
            subscription_type=self.subscription_type,
            is_active=True,
            start_date__lte=self.end_date,
            end_date__gte=self.start_date
        )

        if overlapping_subscriptions.exists():
            existing_subscription = overlapping_subscriptions.first()
            # Formatea las fechas en formato "dd/mm/yyyy"
            existing_start_date_str = existing_subscription.start_date.strftime('%d/%m/%Y')
            existing_end_date_str = existing_subscription.end_date.strftime('%d/%m/%Y')
            
            error_message = f"Ya existe una suscripción activa que se superpone con estas fechas ({existing_start_date_str} - {existing_end_date_str}). Por favor, elige una fecha que no se superponga."
            raise ValidationError(error_message)

    
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
    subscription = models.ForeignKey(Subscription, on_delete=models.CASCADE, related_name='payments', verbose_name=_('Subscription'))

    # Fields
    price = models.DecimalField(verbose_name=_('Price'), max_digits=10, decimal_places=2)
    date = models.DateTimeField(verbose_name=_('Date'), )

    def __str__(self):
        return f'{self.price} - {self.subscription} - {self.date}'
    
    def clean(self):

        # Verifica si el precio del pago es mayor que el precio de la suscripción
        subscription_price = self.subscription.subscription_type.price
        if self.subscription.subscription_type.id == 10:
            pass
        else:
            if self.price > subscription_price:
                raise ValidationError("El precio del pago no puede ser mayor que el precio de la suscripción.")
            if self.price < 0:
                raise ValidationError("El precio del pago no puede ser negativo.")

            # Verifica si ya existe un pago asociado a esta suscripción
            existing_payment = Payment.objects.filter(subscription=self.subscription).first()
            if existing_payment and existing_payment != self:
                raise ValidationError("Ya existe un pago asociado a esta suscripción.")
            
        # Verifica si la fecha del pago es menor que la fecha de inicio de la suscripción
        subscription_start_date = self.subscription.start_date

        if self.date.date() < subscription_start_date:
            formatted_start_date = subscription_start_date.strftime('%d/%m/%Y')
            error_message = f"La fecha del pago no puede ser anterior a la fecha de inicio de la suscripción: {formatted_start_date}"
            raise ValidationError(error_message)

        super().clean()

    
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
auditlog.register(User)