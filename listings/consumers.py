#consumers.py
import json
from channels.generic.websocket import AsyncWebsocketConsumer
from accounts.models import UserAccount
from channels.db import database_sync_to_async

class NotificationConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        print("+++++++++++++++++++CONSUMER++++++++++++++++++++++")
        self.realtor_id = self.scope['url_route']['kwargs']['realtor_id']
        print("realtor_id : ", self.realtor_id)
        realtor = await self.get_realtor_instance()
        print("consumers : ", realtor.id)

        if realtor:
            self.room_group_name = f"notify_{realtor.id}" 
            await self.channel_layer.group_add(
                self.room_group_name,
                self.channel_name
            )
            await self.accept()
            await self.send(text_data=json.dumps({
                'message': 'connected',
            }))

        else:
            await self.close()

    async def get_realtor_instance(self):
        try:
            return await database_sync_to_async(UserAccount.objects.get)(id=self.realtor_id)
        except UserAccount.DoesNotExist:
            return None
    
            

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        await self.send(text_data=json.dumps({'status': 'OK'}))

    async def send_notification(self, event):
        print("+++send_notification")
        data = json.loads(event.get('value'))
        await self.send(text_data=json.dumps({
                'type' : 'notification',
                'payload': data,
                'notification_count': len(data),
            }))
        
    async def logout_user(self, event):
        await self.send(text_data=json.dumps({
            'type': 'logout'
        }))