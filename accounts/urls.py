from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup_user, name='signup-page'),
    path('login/', views.login_user, name='login-page')
]