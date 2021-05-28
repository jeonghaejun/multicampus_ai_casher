from gpiozero import Button, Buzzer
import socket
import net2
import cv2
from signal import pause

IP_ADDRESS = "172.30.1.57"
PORT = 5000

buzzer = Buzzer(21)
button = Button(20)
camera_pin = 0


def to_jpg(frame, quality=80):  # (변환할 이미지)
    encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), quality]
    is_success, jpg = cv2.imencode(".jpg", frame, encode_param)
    return jpg


def streaming():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((IP_ADDRESS, PORT))
        writer = s.makefile('wb')
        while(True):
            cap = cv2.VideoCapture(camera_pin)
            ret, frame = cap.read()
            # cap.capture(frame, format='jpeg', use_video_port=True)
            image = to_jpg(frame)
            net2.send(writer, image)
            # print(frame.shape)
            cap.release()

button.when_pressed = streaming
pause()