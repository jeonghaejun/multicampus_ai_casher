# LED와 PIR 센서를 연결
# 움직임이 감지되면 동영상 녹화 시작, 서버로 이미지 전송
# 움직임이 없어지면 동영상 녹화 중지, 이미지 전송 중지
# 파일명은 날짜_녹화시작시간.h264
# 화면 출력은 없음

from gpiozero import Button, Buzzer
from signal import pause
import picamera
import datetime
import socket
import struct
import threading
import io
import net2

HOST = '192.168.0.4'
PORT = 5000

buzzer = Buzzer(21)
button = Button(20)

camera = picamera.PiCamera()
camera.resolution = (640, 480)
camera.vflip = True

def vido_streaming():
    with socket.socket() as s:
        s.connect((HOST,PORT))
        writer = s.makefile('wb')
        reader = s.makefile('rb')
        stream=io.BytesIO()

        for _ in camera.capture_continuous(stream,'jpeg',use_video_port=True):
            image=stream.getvalue()

            net2.send(writer,image)
            result=net2.receive(reader)[0]
            stream.seek(0)
            stream.truncate()

            if not button.is_pressed:
                writer.write(struct.pack('<L',0))
                writer.flush()
                break



def start_record():
    buzzer.beep(0.1, n=1)
    threading.Thread(target=vido_streaming).start()
    print('recording on')


def stop_record():
    buzzer.beep(0.1, n=1)
    print('recording off')


button.when_pressed = start_record     
button.when_released = stop_record

pause()
