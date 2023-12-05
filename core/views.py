from django.shortcuts import render, redirect, HttpResponse
from .forms import userRegistrationForm, userLoginForm, userProfileForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from .models import UserProfile
from django.contrib.auth.models import Group

# Create your views here.


def userRegister(request):
    if request.method == 'POST':
        form = userRegistrationForm(request.POST)
        if form.is_valid():
            newUser = form.save()
            """ 
            Initially the new user is register to the Research_fellow group
            """
            defaultGroup = Group.objects.get(name='Research_fellow')
            newUser.groups.add(defaultGroup)

            return redirect('dashboard')
    else:
        form = userRegistrationForm()
    return render(request, 'core/register.html', {'form': form})


def userLogin(request):
    if request.method == 'POST':
        form = userLoginForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('dashboard')
    else:
        form = userLoginForm()
    return render(request, 'core/login.html', {'form': form})


def userLogout(request):
    logout(request)
    return redirect('userLogin')
