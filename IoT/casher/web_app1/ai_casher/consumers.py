# chat/consumers.py

from channels.generic.websocket import WebsocketConsumer
import json

class ChatConsumer(WebsocketConsumer):
  	# websocket 연결 시 실행
    def connect(self):
        self.accept()
		# websocket 연결 종료 시 실행 
    def disconnect(self, close_code):
        pass
		# 클라이언트로부터 메세지를 받을 시 실행
    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
				# 클라이언트로부터 받은 메세지를 다시 클라이언트로 보내준다.
        self.send(text_data=json.dumps({
            'message': message
        }))