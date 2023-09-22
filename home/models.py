from django.db import models

# Create your models here.


class Student(models.Model):

    first_name = models.CharField(max_length=50)
    second_name = models.CharField(max_length=50)
    first_surname = models.CharField(max_length=50)
    second_surname = models.CharField(max_length=50)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    address = models.CharField(max_length=200)
    birthdate = models.DateField()

    def __str__(self):
        return f"{self.first_name} {self.first_surname}"
    
class Educator(models.Model):

    first_name = models.CharField(max_length=50)
    second_name = models.CharField(max_length=50)
    first_surname = models.CharField(max_length=50)
    second_surname = models.CharField(max_length=50)
    
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    address = models.CharField(max_length=200)
    id_document = models.CharField(max_length=50)
    birthdate = models.DateField()

    def __str__(self):
        return f"{self.first_name} {self.first_surname}"
    
# Lesson: Piano, Cuatro, etc.
class Lesson(models.Model):

    name = models.CharField(max_length=50)
    
    def __str__(self):
        return f"{self.name}"