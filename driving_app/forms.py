from django import forms
from . models import Appointment
# my forms

class AppointmentForm(forms.Form):
    courses = (
        ('auto', 'Automatic car lessons'),
        ('highway', 'Highway driving lesson'),
        ('international', 'International driving ')
    )
    cars = (
        ('sedan', 'Sedan'),
        ('truck', 'Truck')
    )
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Your Name', 'class': 'form-control border-0'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Your Email', 'class': 'form-control border-0'}))
    course_type = forms.CharField(widget=forms.Select(attrs={'choices': 'courses', 'class': 'form-control border-0', 'placeholder': 'Click to choose Course Type'}, choices=courses))
    car_type = forms.CharField(widget=forms.Select(attrs={'placeholder': 'Click to choose Car Type', 'class': 'form-control border-0'}, choices=cars))
    message = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Message', 'class': 'form-control border', 'rows': '8'}))