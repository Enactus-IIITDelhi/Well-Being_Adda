from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from . import forms

def index(request):
    return render(request, "chat_feature/index.html")


def chat_index(request):
    return render(request, 'chat_feature/chat_index.html')


def room(request, room_name):
    return render(request, 'chat_feature/chat_room.html', {
        'room_name': room_name
    })


def register(request):
    if request.method == "GET":
        return render(
            request, "chat_feature/register.html",
            {"form": forms.CustomUserCreationForm}
        )
    elif request.method == "POST":
        form = forms.CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(reverse("index"))
