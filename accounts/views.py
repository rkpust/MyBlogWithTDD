from django.shortcuts import render, redirect
from .forms import UserRegistrationForm
from django.urls import reverse

# Create your views here.
def signup_user(request):
    form = UserRegistrationForm()

    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('login-page')

    context = {
        'form': form,
        'title': 'Registration Form'
    }
    return render(request, 'accounts/register.html', context)



def login_user(request):
    return render(request, 'accounts/login.html')