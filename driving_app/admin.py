from django.contrib import admin

from .models import Appointment
# Register your models here.

class AdminAppointment(admin.ModelAdmin):
    list_display = [
        'name',
        'email',
        'course_type',
        'car_type',
        'message'
    ]