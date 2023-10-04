from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup_user, name='signup-page')
]