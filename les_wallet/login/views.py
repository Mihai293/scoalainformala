from django.contrib.auth.forms import UserCreationForm
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

def logout_user(request):
    logout(request)
    messages.success(request, "Succes")
    return redirect ('wallet_pag:wallet')

def register_user(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, ("Registration Succes !"))
            return redirect('wallet_pag:wallet')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {
       "form": form,
    })