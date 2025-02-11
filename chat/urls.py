from django.urls import path
from . import views

urlpatterns = [
    path('room/<int:chat_id>/', views.chat_room, name='chat_room'),
    path('delete/<int:message_id>/', views.delete_message, name='delete_message'),
    path('chat_with/<int:user_id>/', views.get_or_create_chat_room, name='get_or_create_chat_room'),
    path('profile/<str:username>/', views.profile_view, name='profile_view')

]

