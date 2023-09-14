import asyncio
import json
from celery import shared_task, states, Celery
from celery.exceptions import Ignore
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from .models import BroadcastNotification


@shared_task(bind=True)
def broadcast_notification(self, data):
    print(data)
    try:
        notification = BroadcastNotification.objects.filter(id=int(data))
        if len(notification) > 0:
            notification = notification.first()
            channel_layer = get_channel_layer()
            event_loop = asyncio.new_event_loop()
            asyncio.set_event_loop(event_loop)
            event_loop.run_until_complete(channel_layer.group_send)(
                'notification_broadcast',
                {
                    'type': 'send_broadcast_notification',
                    'message': 'message'
                }
            )
            notification.status= 's'
            notification.save()
            return 'done'
        else:
            self.update_state(
                state = 'FAILURE',
                meta = {'exe' : 'not found'}
            )
            raise Ignore()
    except:
        pass
 