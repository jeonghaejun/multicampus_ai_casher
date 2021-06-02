from gpiozero import LED
import spidev
import RPi.GPIO as GPIO
import time

led = LED(16)
spi = spidev.SpiDev()
spi.open(0, 0)
spi.max_speed_hz = 1350000

channel1 = 0
velocity = 70


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


def analog_read(channel):
    r = spi.xfer2([1, (8 + channel) << 4, 0])
    adc_out = ((r[1] & 3) << 8) + r[2]
    return adc_out


def forword():
    # print('dc motor start')
    GPIO.output(In1, GPIO.LOW)
    GPIO.output(In2, GPIO.HIGH)
    GPIO.output(In3, GPIO.LOW)
    GPIO.output(In4, GPIO.HIGH)
    pwm.ChangeDutyCycle(velocity)
    pwm2.ChangeDutyCycle(velocity)


def stop():
    # print('dc motor stop')
    GPIO.output(In1, GPIO.HIGH)
    GPIO.output(In2, GPIO.HIGH)
    pwm.ChangeDutyCycle(velocity)


try:
    while True:
        time.sleep(0.1)
        reading1 = analog_read(channel1)
        # print(reading1)
        # print(reading2)
        if reading1 <= 1000:
            # forword()
            # # print('dc motor start')
            GPIO.output(In1, GPIO.LOW)
            GPIO.output(In2, GPIO.HIGH)
            GPIO.output(In3, GPIO.LOW)
            GPIO.output(In4, GPIO.HIGH)
            pwm.ChangeDutyCycle(velocity)
            pwm2.ChangeDutyCycle(velocity)
            time.sleep(20)
        else:
            # stop()
            # # print('dc motor stop')
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
