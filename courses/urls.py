from django.urls import path
from . import views

app_name = 'courses'

urlpatterns = [
    path('', views.course_list, name='courses'),
    path('enroll/', views.enroll_course, name='enroll_course'),
]
