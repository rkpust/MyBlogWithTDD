from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='homepage'),
    path('post/<int:id>/', views.PostDetail, name='post-detail'),
    path('create_post/', views.create_post, name='create_post'),
]