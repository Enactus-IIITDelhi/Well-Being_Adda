from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from .models import Message, Contact
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


def get_last_10_messages():
    messages = Message.objects.order_by('-timestamp').all()[:10]
    return messages


def get_user_contact(username):
    user = get_object_or_404(User, username=username)
    return get_object_or_404(Contact, user=user)
