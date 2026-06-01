from django.urls import path
from . import views

urlpatterns = [
    path('privacy-policy/', views.privacy_policy_view, name='privacy_policy'),
]