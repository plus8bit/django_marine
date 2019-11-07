from django.shortcuts import render


def signup_views(request):
    return render(request, 'accounts/signup.html')
