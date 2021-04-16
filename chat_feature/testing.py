from os import name
from .models import Chat

chat = Chat.objects.get(name="test_chat")
users = chat.participants.all()
print(users)