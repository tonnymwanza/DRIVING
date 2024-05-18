from django.contrib import admin

from .models import Appointment
from . models import Contact
from . models import Course
from . models import Application
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

@admin.register(Course)
class AdminCourse(admin.ModelAdmin):
    list_display = [
        'name',
        'price',
        'description',
        'image'
    ]


admin.site.register(Application)