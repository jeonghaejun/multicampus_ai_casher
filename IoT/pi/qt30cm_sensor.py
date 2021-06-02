from gpiozero import LED
import spidev
import time

led = LED(16)
spi = spidev.SpiDev()
spi.open(0, 0)
spi.max_speed_hz = 1350000

channel1 = 0
# channel2 = 1


def analog_read(channel):
    r = spi.xfer2([1, (8 + channel) << 4, 0])
    adc_out = ((r[1] & 3) << 8) + r[2]
    return adc_out


while True:
    time.sleep(1)
    reading1 = analog_read(channel1)
    # reading2 = analog_read(channel2)
    print(reading1)
    # print(reading2)
    if reading1 <= 1000:
        led.on()
    else:
        led.off()
