from django.urls import path

from base_pages import views
from diploma_pages import views

urlpatterns = [
    path('courses/', views.CoursesPage.as_view(), name='diplomaques'),
]