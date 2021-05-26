import socket
import struct
import io
from PIL import Image

server_socket = socket.socket()
server_socket.bind(('0.0.0.0', 8000))
server_socket.listen(0)

connection = server_socket.accept()[0].makefile('rb')

try:
    while True:
        # 이미지 길이 확인
        image_len = struct.unpack('<L', connection.read(struct.calcsize('<L')))[0]

        if not image_len:
            break

        # 이미지 길이만큼 데이터 읽기
        image_stream = io.BytesIO()
        image_stream.write(connection.read(image_len))

        # 이미지 읽기 위해 처음으로 되감기
        image_stream.seek(0)
        image = Image.open(image_stream)

        image.verify()

finally:
    connection.close()
    server_socket.close()