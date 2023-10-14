from django.db import models

class Student(models.Model):
    first_name = models.CharField(max_length=50)
    second_name = models.CharField(max_length=50, blank=True, null=True)
    first_surname = models.CharField(max_length=50)
    second_surname = models.CharField(max_length=50, blank=True, null=True)
    birthdate = models.DateField()
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()
    address = models.CharField(max_length=200)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.first_name} {self.first_surname}"

class Teacher(models.Model):
    identify_card = models.CharField(max_length=20)
    first_name = models.CharField(max_length=50)
    second_name = models.CharField(max_length=50, blank=True, null=True)
    first_surname = models.CharField(max_length=50)
    second_surname = models.CharField(max_length=50, blank=True, null=True)
    birthdate = models.DateField()
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()
    address = models.CharField(max_length=200)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.first_name} {self.first_surname}"

class Lesson(models.Model):
    name = models.CharField(max_length=50)
    cost = models.DecimalField(max_digits=8, decimal_places=2)
    type = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name} {self.cost} {self.type}"
    
class TeacherXLesson(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)

class Subscription(models.Model):
    total_amount = models.DecimalField(max_digits=8, decimal_places=2)
    subscription_status = models.CharField(max_length=50)
    start_date = models.DateField()
    end_date = models.DateField()
    description = models.CharField(max_length=200)


    def __str__(self):
        return f"{self.total_amount}"

class StudentXLessonXSubscription(models.Model):
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    description = models.CharField(max_length=200, blank=True, null=True)
    student_status = models.CharField(max_length=50, blank=True, null=True)

    student = models.ForeignKey(Student, on_delete=models.CASCADE, blank=True, null=True)
    subscription = models.ForeignKey(Subscription, on_delete=models.CASCADE, blank=True, null=True)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return f"{self.student} - {self.subscription}"
    

class Renew(models.Model):
    Subscription_amount = models.DecimalField(max_digits=8, decimal_places=2)
    end_date = models.DateTimeField()
    number_of_months = models.PositiveIntegerField()

    subscription = models.ForeignKey(Subscription, on_delete=models.CASCADE)

class Payment(models.Model):
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True)
    payment_date = models.DateTimeField(auto_now_add=True)

    subscription = models.ForeignKey(Subscription, on_delete=models.CASCADE)

    def __str__(self):
        return f"Payment of {self.amount} on {self.payment_date}"