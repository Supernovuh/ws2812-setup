#most the setup I use for controlling neopixels
#imports
import time, machine, neopixel, gc

#define important bits
pin = 1
led_num = 37

#setup
np = neopixel.NeoPixel(machine.Pin(pin), led_num)