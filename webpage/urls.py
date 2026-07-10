from django.urls import path
from . import views

urlpatterns = [
    path('', views.calendar, name='calendar'),
    path('events/', views.event_list, name='event_list'),
    path('add/', views.add_event, name='add_event'),
]