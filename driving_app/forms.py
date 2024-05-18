from django import forms

from . models import Contact
from . models import Application
from . models import Appointment
from . models import Course
# my forms

class AppointmentForm(forms.Form):
    courses = (
        ('auto', 'Automatic car lessons'),
        ('highway', 'Highway driving lesson'),
        ('international', 'International driving ')
    )
    cars = (
        ('sedan', 'Sedan'),
        ('truck', 'Truck'),
        ('bus', 'Bus')
    )
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Your Name', 'class': 'form-control border-0'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Your Email', 'class': 'form-control border-0'}))
    course_type = forms.CharField(widget=forms.Select(attrs={'choices': 'courses', 'class': 'form-control border-0', 'placeholder': 'Click to choose Course Type'}, choices=courses))
    car_type = forms.CharField(widget=forms.Select(attrs={'placeholder': 'Click to choose Car Type', 'class': 'form-control border-0'}, choices=cars))
    message = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Message', 'class': 'form-control border', 'rows': '8'}))

class ContactForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control border-0 bg-light'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control border-0 bg-light'}))
    subject = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control border-0 bg-light'}))
    message = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control border-0 bg-light', 'height': '150px'}))

class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = [
            'course',
            'time',
            'age', 
            'country'
        ]
        countries = (
            ('kenya', 'Kenya'),
            ('uganda', 'Uganda'),
            ('tanzania', 'Tanzania'),
            ('burundi', 'Burundi')
        )
        course = forms.ModelMultipleChoiceField(queryset=Course.objects.all(), widget=forms.RadioSelect)
        time = forms.CharField()
        age = forms.IntegerField()
        country = forms.CharField(widget=forms.RadioSelect())