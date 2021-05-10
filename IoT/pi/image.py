from gpiozero import Button, Buzzer
import socket
import net2
from signal import pause
import cv2

IP_ADDRESS = "172.30.1.121"
PORT = 5000

buzzer = Buzzer(21)
button = Button(20)
camera_pin = 0


def to_jpg(frame, quality=80):  # (변환할 이미지)
    encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), quality]
    is_success, jpg = cv2.imencode(".jpg", frame, encode_param)
    return jpg


def picture():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((IP_ADDRESS, PORT))
        writer = s.makefile('wb')
        cap = cv2.VideoCapture(camera_pin)
        ret, image = cap.read()
        print(ret)
        print(image.shape)
        if not ret:
            print('doorlock실패-----------------------------')
            return
        image = to_jpg(image)
        net2.send(writer, image)
        cap.release()

    buzzer.beep(0.1, n=1)


button.when_pressed = picture
pause()
