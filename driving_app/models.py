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

class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    subject = models.CharField(max_length=50)
    message = models.TextField()
