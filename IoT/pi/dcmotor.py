import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

Ena = 16
In1 = 20
In2 = 21

GPIO.setup(Ena, GPIO.OUT)
GPIO.setup(In1, GPIO.OUT)
GPIO.setup(In2, GPIO.OUT)

pwm = GPIO.PWM(Ena, 100)
pwm.start(0)

while True:
    GPIO.output(In1, GPIO.LOW)
    GPIO.output(In2, GPIO.HIGH)
    pwm.ChangeDutyCycle(100)
    sleep(2)

    GPIO.output(In1, GPIO.HIGH)
    GPIO.output(In2, GPIO.LOW)
    pwm.ChangeDutyCycle(100)
    sleep(2)