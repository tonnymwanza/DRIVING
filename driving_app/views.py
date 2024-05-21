from django.shortcuts import render
from django.shortcuts import redirect
from django.views import View
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib import auth
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin

from . models import Contact
from . forms import AppointmentForm
from . models import Appointment
from . forms import ContactForm
from . models import Course
from . models import Application
from . forms import ApplicationForm
# Create your views here.

class HomeView(View):

    def get(self, request):
        course_obj = Course.objects.all()
        form = AppointmentForm(request.GET)
        context = {
            'form': form,
            'course_obj': course_obj
        }
        return render(request, 'index.html', context)

class AboutView(View):

    def get(self, request):
        return render(request, 'about.html')
    
class CourseView(View):

    def get(self, request):
        course_obj = Course.objects.all()
        context = {
            'course_obj': course_obj
        }
        return render(request, 'courses.html', context)
    
class ContactView(View):

    def get(self, request):
        form = ContactForm(request.GET)
        context = {
            'form': form
        }
        return render(request, 'contact.html', context)
    
    def post(self, request):
        form = ContactForm(request.POST)
        if form.is_valid():
            contact_obj = Contact.objects.create(
                name = form.cleaned_data['name'],
                email =form.cleaned_data['email'],
                subject = form.cleaned_data['subject'],
                message = form.cleaned_data['message']
            )
            messages.info(request, 'thanks for sending the message. we will get back to you soon')
        else:
            messages.error(request, 'error sending info. try again')
        return redirect('contact')

def register(request):
    if request.method == 'POST':
        firstname = request.POST['firstname']
        username = request.POST['username']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(username = username).exists():
                messages.info(request, 'the username is taken')
                return redirect('register')
            else:
                user  = User.objects.create_user(first_name = firstname, username = username, password = password)
                return redirect('login')
        else:
            messages.error(request, 'the password dont match')
            return redirect('register')
    return render(request, 'register.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(username = username, password = password)
        if user is not None:
            auth.login(request, user)
            if 'next' in request.POST:
                return redirect(request.POST['next'])
            else:
                return redirect('index')
        else:
            messages.error(request, 'invalid credentials')
            return redirect('login')
    return render(request, 'login.html')

def appointment(request):
    form = AppointmentForm(request.POST or None)
    if form.is_valid():
        apoint_obj = Appointment.objects.create(
            name = form.cleaned_data['name'],
            email = form.cleaned_data['email'],
            course_type = form.cleaned_data['course_type'],
            car_type = form.cleaned_data['car_type'],
            message = form.cleaned_data['message']
        )
        messages.info(request, 'thanks for submitting your details')
    else:
        messages.error(request, 'problem encountered while sending the details')
    return redirect('index')

class ApplicationView(LoginRequiredMixin, View):
    login_url = 'login'
    def get(self, request, pk):
        courses = Course.objects.get(id=pk)
        form = ApplicationForm(request.GET)
        context = {
            'form': form
        }
        return render(request, 'application.html', context)
    
    def post(self, request, pk):
        errors = None
        course = Course.objects.get(id=pk)
        user = request.user
        form = ApplicationForm(request.POST)
        if form.is_valid():
            application = Application.objects.create(
                course = course,
                user = user,
                time = form.cleaned_data['time'],
                age = form.cleaned_data['age'],
                county = form.cleaned_data['county'],
                name = form.cleaned_data['name'],
                id_no = form.cleaned_data['id_no'],
                phone_number = form.cleaned_data['phone_number'],
                email = form.cleaned_data['email']
            )
            messages.success(request, 'application complete')
        else:
            # form.errors:
            errors = form.errors
        # else:
            # messages.error(request, 'application failed')
        context = {
            'form': form,
            'errors': errors
        }
        return redirect('application', pk=pk)