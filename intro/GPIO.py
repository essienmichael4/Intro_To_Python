from gpiozero import LED
from time import sleep

led1 = LED(17)
led2 = LED(22)
led3 = LED(10)

while True:
    led3.on()
    sleep(3)
    led3.off()

    led2.on()
    sleep(0.5)
    led2.off()

    led1.on()
    sleep(3)
    led1.off()
