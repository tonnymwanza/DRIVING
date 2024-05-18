from django import forms
from . models import Appointment
# my forms

class AppointmentForm(forms.Form):
    courses = (
        ('auto', 'Automatic car lessons'),
        ('highway', 'Highway driving lesson'),
        ('international', 'International driving ')
    )
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Your Name', 'class': ''}))
    email = forms.EmailField()
    course_type = forms.CharField(widget=forms.RadioSelect(choices=courses, attrs={''}))
    cart_type = forms.CharField()
    message = forms.CharField()