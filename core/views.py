from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import *
from .forms import PhotoForm

def home(request):
    images = Photo.objects.all()

    context = {
        'images': images
    }
    return render(request, 'home.html', context)

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {
        'form': form
    })

def upload(request):
    form = PhotoForm(request.POST, request.FILES or None)
    if form.is_valid():
        instance = form.save(commit=False)
        if request.user.is_anonymous:
            instance.save()
        else:
            instance.owner = request.user
            instance.save()
        return redirect('home')

    context = {
        'form': form
    }

    return render(request,'upload.html',context)
