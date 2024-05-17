from django.shortcuts import render
from django.shortcuts import redirect
from django.views import View
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib import auth
from django.contrib import messages

# Create your views here.

class HomeView(View):

    def get(self, request):
        return render(request, 'index.html')

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