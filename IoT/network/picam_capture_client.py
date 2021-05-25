import io
import socket
import struct
import time
import picamera

# 서버에 연결
client_socket = socket.socket()
client_socket.connect(('project_server', 8000))

# 연결에서 파일과 같은 객체 만들기
connection = client_socket.makefile('wb')
try:
    camera = picamera.PiCamera()
    camera.resolution = (1024, 768)
    camera.start_preview()
    time.sleep(2)

    start = time.time()
    stream = io.BytesIO()

    for _ in camera.capture_continuous(stream, 'jpeg'):
        # 이미지 길이 쓴 후 전송
        connection.write(struct.pack('<L', stream.tell()))
        connection.flush()

        # 스트림을 되감고, 이미지를 전송
        stream.seek(0)
        connection.write(stream.read())

        # 다음 캡쳐를 위한 스트림 리셋
        stream.seek(0)
        stream.truncate()

        # 메세지의 끝을 알리는 길이 0값 기록
        connection.write(struct.pack('<L', 0))

finally:
    connection.close()
    client_socket.close()