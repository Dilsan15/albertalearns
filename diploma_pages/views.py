from django.shortcuts import render
from django.views.generic import TemplateView


class CoursesPage(TemplateView):
    template_name ="diploma_prep/courses.html"