import RPi.GPIO as GPIO
from time import sleep

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
pwm2 = GPIO.PWM(Enb,100)
pwm2.start(0)


try:
    while True:

        # print('dc motor forward')
        GPIO.output(In1, GPIO.LOW)
        GPIO.output(In2, GPIO.HIGH)
        GPIO.output(In3, GPIO.LOW)
        GPIO.output(In4, GPIO.HIGH)
        pwm.ChangeDutyCycle(100)
        pwm2.ChangeDutyCycle(100)
        # print('dc motor forward')
        

        # print('dc motor backward')
        # GPIO.output(In1, GPIO.HIGH)
        # GPIO.output(In2, GPIO.LOW)
        # pwm.ChangeDutyCycle(100)
        # # print('dc motor backward')
        # sleep(3)

        # print('dc motor stop')
        # GPIO.output(In1, GPIO.HIGH)
        # GPIO.output(In2, GPIO.HIGH)
        # pwm.ChangeDutyCycle(100)
        # # print('dc motor backward')
        # sleep(3)

except KeyboardInterrupt:
    pass
pwm.stop()
pwm2.stop()
GPIO.cleanup()
