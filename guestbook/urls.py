from django.urls import path
from . import views

urlpatterns = [
    path('guestbook/', views.guestbook_view, name='guestbook'), # 주소는 /accounts/signup/ 이 됩니다.
]