from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import JsonResponse

def register(request):
    if request.method == 'POST':
        # Get form data from the request
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')

        # Validate form data
        if User.objects.filter(username=username).exists():
            return render(request, 'register.html', {'error': 'Username already exists'})
        if User.objects.filter(email=email).exists():
            return render(request, 'register.html', {'error': 'Email already in use'})

        # Create new user
        user = User.objects.create_user(username=username, password=password, email=email)
        user.save()
        return redirect('login')  # Redirect to login page after successful registration

    return render(request, 'register.html')

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/todo')  # Redirect to /todo after successful login
        else:
            return render(request, 'login.html', {'error': 'Invalid username or password'})

    return render(request, 'login.html')

def user_logout(request):
    logout(request)
    return redirect('login')
