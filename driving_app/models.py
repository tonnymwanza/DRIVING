from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Appointment(models.Model):
    appointee = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=50)
    email = models.EmailField()
    course_type = models.CharField(max_length=50)
    car_type = models.CharField(max_length=50)
    message = models.TextField()

    def __str__(self):
        return self.name

class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    subject = models.CharField(max_length=50)
    message = models.TextField()

    def __str__(self):
        return self.name

class Course(models.Model):
    name = models.CharField(max_length=150)
    price = models.DecimalField(max_digits=9, decimal_places=2)
    description = models.TextField()
    image = models.ImageField(null=True)
    duration = models.IntegerField(null=True)

    def __str__(self):
        return self.name
    

class Application(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, null=True, unique=False, blank=True)
    time = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    age = models.IntegerField()
    country = models.CharField(max_length=50)

