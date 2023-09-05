from machine import Pin
import time

# Declare the pins and the pin mode
red_led = Pin(18, Pin.OUT)
yellow_led = Pin(17, Pin.OUT)
green_led = Pin(16, Pin.OUT)

# Begin looping phase
while True:
    # Turn on all leds and wait 2 seconds
    green_led.high()
    yellow_led.high()
    red_led.high()
    time.sleep(2)

    # Turn green led off and wait 2 seconds
    green_led.low()
    time.sleep(2)

    # Turn red led off and wait 2 seconds
    yellow_led.low()
    time.sleep(2)

    # Turn yellow led off and wait 2 seconds
    red_led.low()
    time.sleep(2)
