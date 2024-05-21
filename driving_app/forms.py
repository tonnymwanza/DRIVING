from django import forms

from . validators import age_validator
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

class ApplicationForm(forms.Form):
    time_choice = (
        ('evening', 'Evening'),
        ('morning', 'Morning')
    )
    county_choice = (
        ('nairobi', 'Nairobi'),
        ('bungoma', 'Bungoma'),
        ('machakos', 'Machakos'),
        ('kisumu', 'Kisumu')
    )
    time = forms.CharField(widget=forms.Select(attrs={'placeholder':'select morning or evening'}, choices=time_choice))
    age = forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder': 'enter your age'}))
    county = forms.CharField(widget=forms.RadioSelect(choices=county_choice))
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'enter your name'}))
    id_no = forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder': 'your id number'}))
    phone_number = forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder': 'enter your phone number'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'enter your email'}))


    def clean_age(self):
        age = self.cleaned_data.get('age')
        if age < 18:
            raise forms.ValidationError('your age must be above 18')
        return age