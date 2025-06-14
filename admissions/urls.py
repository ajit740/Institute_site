from django.urls import path
from . import views

app_name = 'admissions'

urlpatterns = [
    path('', views.admissions_home, name='admissions'),
    path('process/', views.admission_process, name='admission_process'),
    path('apply/', views.apply, name='apply'),
    path('status/<int:application_id>/', views.application_status, name='application_status'),
]
