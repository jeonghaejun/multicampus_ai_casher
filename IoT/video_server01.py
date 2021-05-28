import net2
import cv2
import numpy as np


IP_ADDRESS_PC = '172.30.1.57'
PORT = 5000


def show_image(data):
    # byte 배열을 numpy로 변환
    data = np.frombuffer(data, dtype=np.uint8)
    image = cv2.imdecode(data, cv2.IMREAD_COLOR)
    key = cv2.waitKey(1)  # 이미지 갱신이 일어나는 곳
    return (image, key)


def receiver(client, addr):
    reader = client.makefile('rb')
    # writer = client.makefile('wb')

    while True:
        data, data_len = net2.receive(reader)
        print('-------수신 ')
        if not data_len:
            return
        # data : jpeg 이미지
        # image : bgr 이미지
        ret, image = show_image(data)
        # AI 알고리즘 처리
        cv2.imshow('image', image)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cv2.destroyAllWindows()
    print('exit receiver')


if __name__ == '__main__':
    net2.server(IP_ADDRESS_PC, PORT, receiver)
    print('start server...')
