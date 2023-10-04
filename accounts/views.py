from django.shortcuts import render

# Create your views here.
def signup_user(request):
    return render(request, 'accounts/register.html')