from .models import BroadcastNotification

def notifications(request):
    all_notifications = BroadcastNotification.objects.all()
    return {'notifications' : all_notifications}