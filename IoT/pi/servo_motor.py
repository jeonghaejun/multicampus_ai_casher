import pigpio
from gpiozero import Button
from time import sleep

SERVO = 26
button = Button(24)

pi = pigpio.pi()

while True:
    pi.set_servo_pulsewidth(SERVO, 1500)
    button.wait_for_press()
    
    pi.set_servo_pulsewidth(SERVO, 500)
    sleep(5)


# from gpiozero import Servo
# from gpiozero import Button
# from time import sleep

# servo = Servo(26)
# button = Button(24)

# while True:
#     servo.mid()
#     button.wait_for_press()
#     servo.min()
#     sleep(5)