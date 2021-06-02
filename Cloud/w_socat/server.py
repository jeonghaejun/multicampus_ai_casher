import asyncio
import websockets


async def accept(websocket, path):
    while True:
        data_rcv = await websocket.recv()
        print("received data =" + data_rcv)
        await websocket.send("websock_svr send data ="+data_rcv)


websoc_svr = websockets.serve(accept, "localhost", 3000)

asyncio.get_event_loop().run_until_complete(websoc_svr)
asyncio.get_event_loop().run_forever()
