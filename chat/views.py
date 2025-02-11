from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Chat, Message, Participant

@login_required
def chat_room(request, chat_id):
    chat = get_object_or_404(Chat, id=chat_id)
    if request.method == "POST":
        content = request.POST.get("content")
        if content:
            Message.objects.create(chat=chat, sender=request.user, content=content)
            return redirect('chat_room', chat_id=chat.id)
    messages = chat.messages.filter(is_deleted=False)
    return render(request, 'chat_room.html', {'chat': chat, 'messages': messages})

@login_required
def delete_message(request, message_id):
    message = get_object_or_404(Message, id=message_id, sender=request.user)
    message.is_deleted = True
    message.save()
    return redirect('chat_room', chat_id=message.chat.id)

@login_required
def get_or_create_chat_room(request, user_id):
    other_user = get_object_or_404(User, id=user_id)
    chat = Chat.get_or_create_chat(request.user, other_user)
    return redirect('chat_room', chat_id=chat.id)

def profile_view(request, username):
    user = get_object_or_404(User, username=username)
    return render(request, 'profile.html', {'user': user})

