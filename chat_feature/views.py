from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required, user_passes_test
from django.urls import reverse
from .models import Message, Contact, Chat
from . import forms
from django.core.mail import send_mail, send_mass_mail

universal_chats = list(Chat.objects.filter(universal_chat = True))

def send_invite(emails,sender,room_name):
    msg = f"Hi you have invited to chat by {sender}. The Link is http://localhost:8000/chat/{room_name}/"
    send_mail(
        subject="Invitation to chatroom",
        message=msg,
        from_email=sender,
        recipient_list=emails,
    )

def index(request):
    return render(request, "chat_feature/index.html")


@login_required()
def chat_index(request):
    form = forms.chat_create_form()
    context = {
    }
    context['chats'] = universal_chats
    if request.method == "POST":
        form = forms.chat_create_form(request.POST)
        if form.is_valid():
            room_name = form.cleaned_data['room_name']
            new_chat = Chat(name=room_name)
            new_chat.save()
            emails = form.cleaned_data['emails']
            send_invite(emails,request.user.email,room_name)
            for i in emails:
                user = User.objects.get(email=i)
                contact = Contact.objects.get(user=user)
                new_chat.participants.add(contact)
            new_chat.participants.add(Contact.objects.get(user=request.user))
            return redirect(reverse('chat_feature:room',kwargs={'room_name': room_name}))
    context['form'] = form
    return render(request, 'chat_feature/chat_index.html', context=context)

@login_required()
def room(request, room_name):
    chat = Chat.objects.get(name=room_name)
    if chat in universal_chats:
        contact = Contact.objects.get(user=request.user)
        chat.participants.add(contact)
        chat.save()
        return render(request, 'chat_feature/chat_room.html', {
            'room_name': room_name
        })
    elif chat.participants.filter(user=request.user).exists():
        return render(request, 'chat_feature/chat_room.html', {
            'room_name': room_name
        })
    else:
        return render(request,'chat_feature/no_access.html')


def register(request):
    if request.method == "GET":
        form = forms.contact_creation_form()
        form.order_fields(
            field_order=['username', 'email', 'first_name', 'last_name', 'study', 'no', ''])
        return render(
            request, "chat_feature/register.html",
            {"form": form}
        )
    elif request.method == "POST":
        form = forms.contact_creation_form(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            password = form.cleaned_data['password1']
            study = form.cleaned_data['study']
            no = form.cleaned_data['no']
            user = User(username=username, first_name=first_name,
                        last_name=last_name, password=password)
            user.save()
            contact = Contact(user=user, study=study, no=no)
            contact.save()
            login(request, user)
            return redirect(reverse("chat_feature:home"))
        else:
            return render(
                request, "chat_feature/register.html",
                {"form": forms.contact_creation_form()}
            )

@login_required()
def profile(request):
    if request.method == "GET":
        user = request.user
        contact = Contact.objects.get(user=user)
        chats = contact.chat_set.all()
        cont = {
            "contact": contact,
            'chats':chats
        }
        return render(request, 'chat_feature/profile.html', context=cont)
    elif request.method == "POST":
        user = request.user
        contact = Contact.objects.get(user=user)
        first_name = request.POST['name'].strip()
        user.first_name = first_name
        user.email = request.POST['email']
        user.username = request.POST['username']
        if request.POST['new_password1'] == request.POST['new_password2'] and len(request.POST['new_password1']) != 0:
            user.set_password(request.POST['new_password1'])
        user.save()
        login(request, user)
        return render(request, 'chat_feature/profile.html')


def about(request):
    return render(request, 'chat_feature/about.html')

