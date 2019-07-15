from gpiozero import LED, Button
from signal import pause
from time import sleep

from subprocess import call
led1 = LED(17)
led2 = LED(22)
led3 = LED(10)

def lights():

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


button = Button(2)
def print_thing():
	led3.on()

	print = ("Button Pressed")

button.when_pressed = print_thing
button.when_released = lights
pause()

