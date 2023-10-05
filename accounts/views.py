from django.shortcuts import render, redirect
from .forms import UserRegistrationForm
from django.urls import reverse
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.
def signup_user(request):
    form = UserRegistrationForm()

    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect(reverse('login-page'))

    context = {
        'form': form,
        'title': 'Registration Form'
    }
    return render(request, 'accounts/register.html', context)



def login_user(request):
    form = AuthenticationForm()

    context = {
        'form': form,
        'title': 'Login Form'
    }

    return render(request, 'accounts/login.html', context)