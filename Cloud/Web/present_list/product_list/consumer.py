from channels.generic.websocket import WebsocketConsumer
import json

class PresentUpload(WebsocketConsumer):
    def connect(self):
        self.accept()

    def disconnect(self, close_code):
        pass

    def recieve(self, item_info):
        item_info_json = json.loads(item_info)
        info = item_info_json['info']

        self.send(item_info_json=json.dumps({
            'info' : info
        }))