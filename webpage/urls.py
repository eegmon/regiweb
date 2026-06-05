from django.urls import path
from . import views

urlpatterns = [
    path('privacy-policy/', views.privacy_policy_view, name='privacy_policy'),
    path('minigame/', views.minigame_view, name='minigame'), # 주소는 /webpage/minigame/ 이 됩니다.
    path('', views.main_view, name='main'), # 메인 페이지 주소는 /webpage/ 입니다.
]