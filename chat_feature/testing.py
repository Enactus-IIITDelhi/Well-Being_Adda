from .models import Contact, Chat
from django.contrib.auth.models import User

chat = Chat.objects.all().delete()
# import chat_feature.testing
