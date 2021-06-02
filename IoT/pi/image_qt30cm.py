from gpiozero import Button, Buzzer, LED
import socket
import net2
import cv2
import spidev
import threading
import time

IP_ADDRESS = "3.35.190.203"
PORT = 8902
# IP_ADDRESS = '172.30.1.89'
# PORT = 5000
# IP_ADDRESS = "18.169.67.45"
# PORT = 8902

buzzer = Buzzer(21)
button = Button(20)
led = LED(16)
camera_pin1 = 2

spi = spidev.SpiDev()
spi.open(0, 0)
spi.max_speed_hz = 1350000
channel1 = 1



def to_jpg(frame, quality=100):  # (변환할 이미지)
    encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), quality]
    is_success, jpg = cv2.imencode(".jpg", frame, encode_param)
    return jpg


def picture1():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((IP_ADDRESS, PORT))
        writer = s.makefile('wb')
        cap = cv2.VideoCapture(camera_pin1)
        ret, image = cap.read()
        image = cv2.rotate(image, cv2.ROTATE_180)

        if not ret:
            print('실패-----------------------------')
            return

        image = to_jpg(image)
        net2.send(writer, image)
        cap.release()

        buzzer.beep(0.1, n=1)


def analog_read(channel):
    r = spi.xfer2([1, (8 + channel) << 4, 0])
    adc_out = ((r[1] & 3) << 8) + r[2]
    return adc_out


while True:
    time.sleep(0.1)
    reading2 = analog_read(channel1)
    
    if reading2 <= 1000:
        led.on()

        t1 = threading.Thread(target=picture1)
        t1.start()

        time.sleep(3)
    else:
        led.off()
