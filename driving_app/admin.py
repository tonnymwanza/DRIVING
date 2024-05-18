from django.contrib import admin

from .models import Appointment
from . models import Contact
# Register your models here.

@admin.register(Appointment)
class AdminAppointment(admin.ModelAdmin):
    list_display = [
        'name',
        'email',
        'course_type',
        'car_type',
        'message'
    ]

@admin.register(Contact)
class AdminContact(admin.ModelAdmin):
    list_display = [
        'name', 
        'email',
        'subject',
        'message'
    ]