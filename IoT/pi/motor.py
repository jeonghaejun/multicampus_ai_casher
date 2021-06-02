from gpiozero import LED
import spidev
import RPi.GPIO as GPIO
import time
from socket import *
import threading

led = LED(16)
spi = spidev.SpiDev()
spi.open(0, 0)
spi.max_speed_hz = 1350000

channel1 = 0
velocity = 60
msg="1"


GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

Ena = 26
In1 = 19
In2 = 13

Enb = 12
In3 = 5
In4 = 6

GPIO.setup(Ena, GPIO.OUT)
GPIO.setup(In1, GPIO.OUT)
GPIO.setup(In2, GPIO.OUT)

GPIO.setup(Enb, GPIO.OUT)
GPIO.setup(In3, GPIO.OUT)
GPIO.setup(In4, GPIO.OUT)


pwm = GPIO.PWM(Ena, 100)
pwm.start(0)
pwm2 = GPIO.PWM(Enb, 100)
pwm2.start(0)

# # 도현
# IP_ADDRESS = "18.169.67.45"
# PORT = 8898

# # 로컬
# IP_ADDRESS = '172.30.1.101'
# PORT = 8898

# 건우
IP_ADDRESS = "3.35.190.203"
PORT = 8898

clientSock = socket(AF_INET, SOCK_STREAM)
clientSock.connect((IP_ADDRESS, PORT))
print('접속 완료')


def analog_read(channel):
    r = spi.xfer2([1, (8 + channel) << 4, 0])
    adc_out = ((r[1] & 3) << 8) + r[2]
    return adc_out

def message():
    global msg
    while True:
        recvData = clientSock.recv(1024)
        msg = recvData.decode('utf-8')
        if msg == "":
            break
        else:
            print('상대방 :', recvData.decode('utf-8'))


t1=threading.Thread(target=message)
t1.start()

try:
    while True:
        time.sleep(0.1)
        reading1 = analog_read(channel1)
        
        if reading1 <= 1000:
            GPIO.output(In1, GPIO.LOW)
            GPIO.output(In2, GPIO.HIGH)
            GPIO.output(In3, GPIO.LOW)
            GPIO.output(In4, GPIO.HIGH)
            pwm.ChangeDutyCycle(velocity)
            pwm2.ChangeDutyCycle(velocity)

            for i in range(100):
                if msg == "0":
                    time.sleep(3)
                    GPIO.output(In1, GPIO.HIGH)
                    GPIO.output(In2, GPIO.HIGH)
                    GPIO.output(In3, GPIO.HIGH)
                    GPIO.output(In4, GPIO.HIGH)
                    pwm.ChangeDutyCycle(velocity)
                    pwm2.ChangeDutyCycle(velocity)
                    msg="1"
                    break
                else:
                    time.sleep(1)
                    
        else:
            GPIO.output(In1, GPIO.HIGH)
            GPIO.output(In2, GPIO.HIGH)
            GPIO.output(In3, GPIO.HIGH)
            GPIO.output(In4, GPIO.HIGH)
            pwm.ChangeDutyCycle(velocity)
            pwm2.ChangeDutyCycle(velocity)


except KeyboardInterrupt:
    pass
pwm.stop()
pwm2.stop()
