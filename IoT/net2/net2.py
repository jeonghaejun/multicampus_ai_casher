import socket
import struct
from _thread import *


def server(ip, port, thread):
    # socket.socket 스레드 함수 참조   / AF_INET은 IPv4 / socket.SOCK_STREAM은 TCP 통신
    with socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM) as s:
        try:
            s.bind((ip, port))
            s.listen(1)
            while True:
                client_socket, addr = s.accept()  # 접속 대기
                # 스레드 기동
                start_new_thread(thread, (client_socket, addr))

        except Exception as e:
            print(e)


def send(writer, data):
    writer.write(struct.pack('<L', len(data)))
    writer.write(data)
    writer.flush()


def receive(reader):
    data = reader.read(struct.calcsize('<L'))
    data_len = struct.unpack('<L', data)[0]

    if not data_len:
        return (None, 0)
    data = reader.read(data_len)

    return (data, data_len)
