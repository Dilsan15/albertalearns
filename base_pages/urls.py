from django.contrib.auth.views import LogoutView
from django.shortcuts import redirect
from django.urls import path, include
from django.views.generic import RedirectView

from albertalearns import settings
from . import views

urlpatterns = [

    path('home/', views.HomePage.as_view(), name='home'),
    path('', RedirectView.as_view(url='home/', permanent=False), name='home_redirect'),

    path('signup/', views.SignUpPage.as_view(), name='signup'),
    path('login/', views.LoginPage.as_view(), name='login'),
    path('logout/', LogoutView.as_view(template_name="user_management/logout_success.html"), name='logout'),

    path('', include('allauth.urls')),
]