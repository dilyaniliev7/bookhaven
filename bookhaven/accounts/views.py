from django.shortcuts import render
from django.views import generic as views
from django.contrib.auth import views as auth_views

# Create your views here.

class SignUpView(views.CreateView):
    pass


class SignInView(auth_views.LoginView):
    pass