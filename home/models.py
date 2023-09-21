from django.db import models

# Create your models here.


class Student(models.Model):

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    address = models.CharField(max_length=200)
    birthdate = models.DateField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"