from machine import Pin
import time

# Declare the pins and the pin mode
red_led = Pin(18, Pin.OUT)
yellow_led = Pin(17, Pin.OUT)
green_led = Pin(16, Pin.OUT)

# Begin looping phase
while True:
    # Turn on the red led for 5 seconds
    green_led.low()
    yellow_led.low()
    red_led.high()
    time.sleep(5)

    # Turn green led on and red led off for 5 seconds
    green_led.high()
    red_led.low()
    time.sleep(5)

    # Turn yellow led on and green led off for 2 seconds
    yellow_led.high()
    green_led.low()
    time.sleep(2)
