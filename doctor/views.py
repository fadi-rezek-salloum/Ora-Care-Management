from django.shortcuts import render
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required

from .models import Doctor
from .forms import LoginForm

class LoginView(auth_views.LoginView):
    form_class = LoginForm
    template_name = 'doctor/login.html' 

class LogoutView(auth_views.LogoutView):
    next_page = '/doctor/login/'