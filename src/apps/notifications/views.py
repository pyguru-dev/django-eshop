from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from django.shortcuts import get_object_or_404
from apps.accounts.models import User

def send_notification(request, user_id):
    user = get_object_or_404(User,pk=user_id)
    
    channel_layer = get_channel_layer()
    
    async_to_sync(channel_layer.group_send)(
        f'user_{user.id}_notification',
        {
            'type' : 'user.notify',
            'notification' : {
                'title' : 'this is title',
                'content' : 'this is content'
            }
        }
    )