from django.db import models
from django.contrib.auth.models import User

class Chat(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    @staticmethod
    def get_or_create_chat(user1, user2):
        chats = Chat.objects.filter(participant__user=user1).filter(participant__user=user2).distinct()
        if chats.exists():
            return chats.first()
        chat = Chat.objects.create()
        Participant.objects.create(chat=chat, user=user1)
        Participant.objects.create(chat=chat, user=user2)
        return chat

class Participant(models.Model):
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('chat', 'user')

class Message(models.Model):
    chat = models.ForeignKey(Chat, related_name="messages", on_delete=models.CASCADE)
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    is_deleted = models.BooleanField(default=False)
 
