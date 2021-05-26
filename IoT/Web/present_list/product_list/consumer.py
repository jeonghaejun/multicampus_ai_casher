from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
import json

class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.show_list = self.scope['url_route']['kwargs']['show_list']
        self.room_group_name = 'chat_%s' % self.show_list

        # "room" 그룹에 가입
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )

        self.accept()

    def disconnect(self, close_code):
        # "room" 그룹에서 탈퇴
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )

    # 웹소켓 으로 부터 메시지 수신
    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        # "room" 그룹에 메시지 전송
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message
            }
        )

    # "room" 그룹에서 메시지 전송
    def chat_message(self, event):
        message = event['message']

        # 웹 소켓으로 메시지 전송
        self.send(text_data=json.dumps({
            'message': message
        }))