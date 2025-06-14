# home/urls.py
from django.urls import path
from . import views

app_name = 'home'  # Required for {% url 'home:index' %}

urlpatterns = [
    path('', views.index, name='index'),       # home:index
    path('about/', views.about, name='about'),
    path('faqs/', views.faqs, name='faqs'),
    path('apply/', views.apply_view, name='apply'),
]
