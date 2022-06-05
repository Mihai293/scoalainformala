from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def login_first(request):
    return render(request, 'templates/enter.html')

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('crypto:coin')
        else:
            messages.success(request,("There was an error logging in, try again"))
            return redirect('login')

    else:
        return render(request, 'enterv1.html')
