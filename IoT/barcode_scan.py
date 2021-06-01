import requests
import json
import asyncio
# 웹 소켓 모듈을 선언한다.
import websockets

async def connect(json_input):
    # 웹 소켓에 접속을 합니다.
    async with websockets.connect("ws://18.169.67.45:8000/ws/chat/1234/") as websocket:
        # 10번을 반복하면서 웹 소켓 서버로 메시지를 전송합니다.
        # await websocket.send('{message: {0}}'.format(json));
        send_msg = {"message": json_input}
        await websocket.send(json.dumps(send_msg));

print("Scan the barcode")
while True:
    scan_in = input("Input :")
    if scan_in is 'q':   # 키보드에서 q 누르고 enter입력하면 종료
        break    
    print("result : " + scan_in)
    

    barcode = scan_in

    url = "https://475pko0wjc.execute-api.eu-west-2.amazonaws.com/dev/barcode/"+ barcode

    #url = "https://www.test.com"


    rs = requests.get(url)
    # response code

    rs_code = rs.status_code


    if int(rs_code) == 200:
        print("Okay")
        rs_text = rs.text
        rs_text = json.loads(rs_text)
        rs_item = rs_text['body'] 
        product = json.loads(rs_item)
        product["Qty"] = 1
        product=[product]
        item_list={"item" : product}
        print(item_list)
        asyncio.get_event_loop().run_until_complete(connect(item_list))

        
    else:
        print(rs_code)
        