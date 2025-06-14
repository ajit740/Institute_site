from django.urls import path
from . import views

app_name = 'events'
urlpatterns = [
    path('', views.events_view, name='event_list'),
    path('register/<int:event_id>/', views.event_register, name='event_register'),
    path('news/<int:news_id>/', views.news_detail, name='news_detail'),
]
