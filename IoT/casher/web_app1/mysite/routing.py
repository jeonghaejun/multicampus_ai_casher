# mysite/routing.py

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
import ai_casher.routing

# 클라이언트와 Channels 개발 서버가 연결 될 때, 어느 protocol 타입의 연결인지
application = ProtocolTypeRouter({
    # (http->django views is added by default)
  	# 만약에 websocket protocol 이라면, AuthMiddlewareStack
    'websocket': AuthMiddlewareStack(
        # URLRouter 로 연결, 소비자의 라우트 연결 HTTP path를 조사
        URLRouter(
            ai_casher.routing.websocket_urlpatterns
        )
    ),
})