from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('signup/', views.signup_view, name='signup'), # 주소는 /accounts/signup/ 이 됩니다.
    path('login/', auth_views.LoginView.as_view(template_name='register/login.html'), name='login'),
]