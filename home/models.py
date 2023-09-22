from django.db import models

class Student(models.Model):
    first_name = models.CharField(max_length=50)
    second_name = models.CharField(max_length=50, blank=True)
    first_surname = models.CharField(max_length=50)
    second_surname = models.CharField(max_length=50, blank=True)
    birthdate = models.DateField()
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()
    address = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.first_name} {self.first_surname}"

class Teacher(models.Model):
    identify_card = models.CharField(max_length=20)
    first_name = models.CharField(max_length=50)
    second_name = models.CharField(max_length=50, blank=True)
    first_surname = models.CharField(max_length=50)
    second_surname = models.CharField(max_length=50, blank=True)
    birthdate = models.DateField()
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()
    address = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.first_name} {self.first_surname}"

class Lesson(models.Model):
    name = models.CharField(max_length=50) 

    def __str__(self):
        return self.name

class LessonType(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class LessonXDetail(models.Model):
    cost = models.DecimalField(max_digits=8, decimal_places=2)

    lesson_type = models.ForeignKey(LessonType, on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.lesson.name} - {self.lesson_type.name}"

class TeacherXDetail(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    lesson_x_detail = models.ForeignKey(LessonXDetail, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.teacher.first_name} - {self.teacher.first_surname}"

class Subscription(models.Model):
    total_amount = models.DecimalField(max_digits=8, decimal_places=2)
    subscription_status = models.CharField(max_length=50)
    start_date = models.DateField()
    end_date = models.DateField()

    student = models.ForeignKey(Student, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.total_amount} - {self.student.first_name} {self.student.first_surname}"

class Payment(models.Model):
    amount_paid = models.DecimalField(max_digits=8, decimal_places=2)
    date = models.DateField()

    subscription = models.ForeignKey(Subscription, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.amount_paid} - {self.date}"

class SubscriptionXDetail(models.Model):
    subscription = models.ForeignKey(Subscription, on_delete=models.CASCADE)
    lesson_x_detail = models.ForeignKey(LessonXDetail, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.subscription.total_amount}"

class RenewSubscription(models.Model):
    subscription_amount = models.DecimalField(max_digits=8, decimal_places=2)
    end_date = models.DateField()
    number_of_months = models.PositiveIntegerField()

    subscription = models.ForeignKey(Subscription, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.subscription_amount} - {self.end_date}"

class StudentXDetail(models.Model):
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    description = models.CharField(max_length=200)
    student_status = models.CharField(max_length=50)

    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subscription = models.ForeignKey(Subscription, on_delete=models.CASCADE)
    lesson_x_detail = models.ForeignKey(LessonXDetail, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.date} - {self.student.first_name} {self.student.first_surname}"
