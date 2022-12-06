# Create your models here.

from django import forms
from allauth.socialaccount.forms import SignupForm
from django.views.generic import TemplateView
from django.contrib.auth.models import User

class MyCustomSocialSignupForm(SignupForm):

    # https://gavinwiener.medium.com/modifying-django-allauth-forms-6eb19e77ef56

    def __init__(self, *args, **kwargs):
        super(MyCustomSocialSignupForm, self).__init__(*args, **kwargs)
        self.fields['email'].widget = forms.HiddenInput()

    def save(self, request):
        user = super(MyCustomSocialSignupForm, self).save(request)
        return user
