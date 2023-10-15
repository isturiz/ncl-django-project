from django.db import models
from django.db.models import UniqueConstraint

class SubscriptionType(models.Model):

    # Fields
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    number_of_lessons = models.IntegerField()

    def __str__(self):
        return f'{self.name} - {self.price} - {self.number_of_lessons}'
    
    class Meta:
        constraints = [
            UniqueConstraint(
                fields=['name', 'price'],
                name='unique_subscription_type'
            )
        ]


class LessonType(models.Model):

    # Fields
    cathedra = models.CharField(max_length=255)
    modality = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.cathedra} - {self.modality}'
    
    class Meta:
        constraints = [
            UniqueConstraint(fields=['cathedra', 'modality'], name='unique_lesson_type')
        ]


class Lesson(models.Model):

    # Foreign Keys
    lesson_type = models.ForeignKey(LessonType, on_delete=models.CASCADE)

    # Fields
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    start_date = models.DateTimeField(blank=True, null=True)
    end_date = models.DateTimeField(blank=True, null=True)
    lesson_status = models.BooleanField(default=True)  # True = Vista, False = No vista

    # M2M
    subscriptions = models.ManyToManyField('Subscription', through='LessonXSubscriptionXTeacher')

    def __str__(self):
        return f'{self.lesson_type} - {self.price} - {self.subscriptions}'


class Teacher(models.Model):

    # Fields
    identify_card = models.CharField(max_length=20, blank=True, null=True)
    first_name = models.CharField(max_length=255)
    second_name = models.CharField(max_length=255, blank=True, null=True)
    first_surname = models.CharField(max_length=255)
    second_surname = models.CharField(max_length=255, blank=True, null=True)
    birthdate = models.DateField()
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()
    address = models.TextField()
    is_active = models.BooleanField(default=True)
    
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
    identify_card = models.CharField(max_length=20, blank=True, null=True)
    first_name = models.CharField(max_length=255)
    second_name = models.CharField(max_length=255, blank=True, null=True)
    first_surname = models.CharField(max_length=255)
    second_surname = models.CharField(max_length=255, blank=True, null=True)
    birthdate = models.DateField()
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()
    address = models.TextField()
    is_active = models.BooleanField(default=True)

    # M2M
    subscriptions = models.ManyToManyField('Subscription', through='SubscriptionXStudentXPayment')

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
    type_subscription = models.ForeignKey(SubscriptionType, on_delete=models.CASCADE)

    # Fields
    start_date = models.DateField()
    end_date = models.DateField()
    subscription_status = models.BooleanField(default=True, blank=True, null=True)

    # M2M
    students = models.ManyToManyField('Student', through='SubscriptionXStudentXPayment')
    lessons = models.ManyToManyField('Lesson', through='LessonXSubscriptionXTeacher')

    def __str__(self):
        return f'{self.type_subscription} - {self.students} - {self.lessons}'


class Payment(models.Model):

    # Fields
    price = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True)

    # M2M
    subscriptions = models.ManyToManyField('Subscription', through='SubscriptionXStudentXPayment')

    def __str__(self):
        return f'{self.price} - {self.subscriptions} - {self.date}'
    

class LessonXSubscriptionXTeacher(models.Model):

    # Foreign Keys
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    subscription = models.ForeignKey(Subscription, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.lesson} - {self.subscription} - {self.teacher}'


class SubscriptionXStudentXPayment(models.Model):

    # Foreign Key
    subscription = models.ForeignKey(Subscription, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    payment = models.ForeignKey(Payment, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return f'{self.subscription} - {self.student} - {self.payment}'
    
