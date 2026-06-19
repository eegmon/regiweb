from django.urls import path

from . import views

urlpatterns = [
    path('', views.gallery_page, name='gallery_page'),
    path('api/posts/', views.post_list_api, name='gallery_post_list_api'),
    path('api/posts/create/', views.post_create_api, name='gallery_post_create_api'),
]
