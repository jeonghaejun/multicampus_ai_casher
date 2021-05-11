import net2
import json

import cv2
import numpy as np

HOST = '172.30.1.96'
PORT = 5000

counter = 0


def show_image(data,frame_name):
    # byte 배열을 numpy로 변환
    data = np.frombuffer(data, dtype=np.uint8)
    image = cv2.imdecode(data, cv2.IMREAD_COLOR)
    # Video.show()
    cv2.imshow(frame_name, image)
    cv2.waitKey(1)  # 이미지 갱신이 실제 일어나는 곳.


def receiver(client, addr):
    global counter
    counter += 1  # 스레드 별로 imshow에서 사용할 타이틀을 다르게 하기 위해서
    frame_name=f'frame{counter}'

    reader = client.makefile('rb')
    writer = client.makefile('wb')
    while True:
        data, data_len = net2.receive(reader)
        if not data:
            break
        # print('received ', data_len)  # 이미지 처리
        # AI 알고리즘 처리 - 불량 여부 판단... 여기에 넣으면됭
        show_image(data,frame_name)
        result = json.dumps({'result': 'ok'})
        net2.send(writer, result.encode())

    print('exit receiver')


if __name__ == '__main__':
    print('start server...')
    net2.server(HOST, PORT, receiver)
