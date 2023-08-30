from machine import Pin
import time
# Declare the pins and the pin mode
red_led = Pin(18, Pin.OUT)
yellow_led = Pin(17, Pin.OUT)
green_led = Pin(16, Pin.OUT)

# Begin looping phase
while True:
    # Turn on all leds and wait 1 second
    green_led.value(0)
    yellow_led.value(0)
    red_led.value(1)
    time.sleep(5)
    # Turn green led off and wait 2 seconds
    green_led.value(1)
    red_led.value(0)
    time.sleep(5)
    # Turn red led off and wait 2 seconds
    yellow_led.value(1)
    green_led.value(0)
    time.sleep(2)
