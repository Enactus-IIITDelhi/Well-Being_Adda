from django.db import models
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
User = get_user_model()


class Contact(models.Model):
    user = models.ForeignKey(
        User, related_name='friends', on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

    def get_user_contact(username):
        user = get_object_or_404(User, username=username)
        return get_object_or_404(Contact, user=user)


class Message(models.Model):
    chat = models.ForeignKey(
        Contact, related_name='messages', on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.contact.user.username


class Chat(models.Model):
    name = models.CharField(max_length=20, primary_key=True)
    participants = models.ManyToManyField(
        Contact, related_name='chats', blank=True)
    messages = models.ManyToManyField(
        Message, blank=True, related_name="message")

    def __str__(self):
        return "{}".format(self.pk)

    def get_last_10_messages(room_name):
        chat = get_object_or_404(Chat, name=room_name)
        return chat.messages.order_by('-timestamp').all()[:10]

    def get_current_chat(room_name):
        return get_object_or_404(Chat, name=room_name)
