from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup_view, name='signup'), # 주소는 /accounts/signup/ 이 됩니다.
]