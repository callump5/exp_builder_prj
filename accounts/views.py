# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

from .forms import SignUpForm, ProfileForm

from .models import Profile
from django.contrib.auth.models import User
# Create your views here.

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('createprofile')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})

def makeprofile(request):
    if request.method == 'POST':

        profileform = ProfileForm(request.POST)
        if profileform.is_valid():
            profile = profileform.save(commit=False)
            profile.user = request.user
            profile.save()
        return redirect('home')
    else:
        profileform = ProfileForm()
    return render(request, 'registration/profile-form.html', {'form': profileform})