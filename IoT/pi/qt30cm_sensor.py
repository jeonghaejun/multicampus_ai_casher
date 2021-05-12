from gpiozero import LED, Buzzer
import spidev

buzzer = Buzzer(21)
led = LED(16)
spi = spidev.SpiDev()
spi.open(0, 0)
spi.max_speed_hz = 1350000


def analog_read(channel):
    r = spi.xfer2([1, (8 + channel) << 4, 0])
    adc_out = ((r[1] & 3) << 8) + r[2]
    return adc_out


while True:
    reading = analog_read(0)
    if reading <= 1000:
        led.on()
    else:
        led.off()
