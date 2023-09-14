import json
from channels.generic.websocket import AsyncJsonWebsocketConsumer, WebsocketConsumer

class NotificationConsumer(AsyncJsonWebsocketConsumer):
    
    async def connect(self):
        self.user = self.scope['user']
        if self.user.is_authenticate:
            await self.accept()
            await self.channel_layer.group_add(
                f'user_{self.user.id}_notification',
                self.channel_name
            )
            
            # await self.channel_layer.group_add(
            #     'user_all_notification',
            #     self.channel_name
            # )            
            
        else:
            await self.close(403)
    
    async def receive_json(self, content, **kwargs):
        pass
    
    async def disconnect(self, code = None):
        pass
    
    async def user_notify(self, data):
        await self.send_json(data['notification'])

class BroadcastNotificationConsumer(AsyncJsonWebsocketConsumer):
    async def connect(self):
        return await super().connect()      
    
    async def disconnect(self, code):
        return await super().disconnect(code)
    
    async def receive_json(self, content, **kwargs):
        return await super().receive_json(content, **kwargs)
    
    async def send_notification(self, event):
        message = json.loads(event['message'])
        await self.send(text_data=json.dumps({
            'message' : message
        }))  
        
class EchoConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()
    
    def disconnect(self, code):
        return super().disconnect(code)
    
    def receive(self, text_data=None, bytes_data=None):
        self.send(text_data=text_data)