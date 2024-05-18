from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views
from . views import ApplicationView
from . views import HomeView
from . views import AboutView
from . views import ContactView
from . views import CourseView
# my urls

urlpatterns = [
    path('', HomeView.as_view(), name='index'),
    path('about_page', AboutView.as_view(), name='about_page'),
    path('course', CourseView.as_view(), name='course'),
    path('contact', ContactView.as_view(), name='contact'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('appointment', views.appointment, name='appointment'),
    path('application/<int:pk>/', ApplicationView.as_view(), name='application'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)