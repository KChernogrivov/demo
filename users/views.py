from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm


# Create your views here.

def home_view(request):
    return render(request, 'users/home.html', {})


def user_login(request):
    if request.user.is_anonymous:
        if request.method == 'POST':
            form = AuthenticationForm(request=request, data=request.POST)
            if form.is_valid():
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']
                user = authenticate(request, username=username, password=password)
                if user is not None:
                    login(request, user)
                    return redirect('home')
            else:
                return render(request, 'users/login.html', {'form': form})
        form = AuthenticationForm()
        return render(request, 'users/login.html', {'form': form})
    else:
        return redirect('home')


def user_logout(request):
    logout(request)
    return redirect('home')
