from django.shortcuts import render
from .forms import UserRegistrationForm

# Create your views here.
def signup_user(request):
    form = UserRegistrationForm()
    context = {
        'form': form,
        'title': 'Registration Form'
    }
    return render(request, 'accounts/register.html', context)