from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.

class LoginPage(TemplateView):
    template_name = 'user_management/login.html'


class SignUpPage(TemplateView):
    template_name = 'user_management/signup.html'


class HomePage(TemplateView):
    template_name = 'home_page/home.html'


