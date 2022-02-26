#most the setup I use for controlling neopixels
#imports
import time, machine, neopixel, gc

#define important bits
pin = 1
led_num = 37
ledPin = 25

#setup
np = neopixel.NeoPixel(machine.Pin(pin), led_num)
led = machine.Pin(ledPin, machine.Pin.OUT)

led.value(1)
