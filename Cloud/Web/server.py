import asyncio
# 웹 소켓 모듈을 선언한다.
import json

import websockets


async def connect(json_input):
    # 웹 소켓에 접속을 합니다.
    async with websockets.connect("ws://127.0.0.1:8000/ws/chat/1234/") as websocket:
        # 10번을 반복하면서 웹 소켓 서버로 메시지를 전송합니다.
        # await websocket.send('{message: {0}}'.format(json));
        send_msg = {"message": json_input}
        await websocket.send(json.dumps(send_msg));


# 웹 소켓 서버로 부터 메시지가 오면 콘솔에 출력합니다.
# 비동기로 서버에 접속한다.

item_list = {"item": [

    {

        "id": 11879,

        "name": "샌드위치",

        "price": 3000,

        "Qty": 1

    },

    {

        "id": 11880,

        "name": "츄파츕스",

        "price": 300,

        "Qty": 2

    }

]

}
asyncio.get_event_loop().run_until_complete(connect(item_list))
# asyncio.run(connect(item_list))
