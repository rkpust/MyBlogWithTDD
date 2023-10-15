from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('signup/', views.signup_user, name='signup-page'),
    path('login/', views.login_user, name='login-page'),
    path('logout/', views.logout_user, name='logout'),
    path('password_reset/', auth_views.PasswordResetView.as_view(
        template_name = 'accounts/password-reset.html'
    ), name='password-reset'),
    path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(
        template_name = 'accounts/password-reset-done.html'
    ), name='password_reset_done'),
    path('reset/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(
        template_name = 'accounts/password-reset-confirm.html'
    ), name='password_reset_confirm'),
    path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(
        template_name = 'accounts/password-reset-complete.html'
    ), name='password_reset_complete'),
]