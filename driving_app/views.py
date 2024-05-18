from django.shortcuts import render
from django.shortcuts import redirect
from django.views import View
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib import auth
from django.contrib import messages

from . forms import AppointmentForm
from . models import Appointment
# Create your views here.

class HomeView(View):

    def get(self, request):
        form = AppointmentForm(request.GET)
        context = {
            'form': form
        }
        return render(request, 'index.html', context)

class AboutView(View):

    def get(self, request):
        return render(request, 'about.html')
    
class CourseView(View):

    def get(self, request):
        return render(request, 'courses.html')
    
class ContactView(View):

    def get(self, request):
        return render(request, 'contact.html')
    
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
                return redirect(request.POST[next])
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