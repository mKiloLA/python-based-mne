from machine import Pin
import time

# Declare the pins and the pin mode
red_led = Pin(18, Pin.OUT)
yellow_led = Pin(17, Pin.OUT)
green_led = Pin(16, Pin.OUT)

def set_lights(on):
    '''Set lights on or off.

    Args:
        on (int): 1 for on and 0 for off
    
    Returns:
        None
    '''
    green_led.value(on)
    yellow_led.value(on)
    red_led.value(on)

# Begin looping phase
while True:
    for i in range(0, 3):
        set_lights(1)
        time.sleep(0.5)
        set_lights(0)
        time.sleep(0.5)

    for i in range(0, 3):
        set_lights(1)
        time.sleep(1.5)
        set_lights(0)
        time.sleep(0.5)

    for i in range(0, 3):
        set_lights(1)
        time.sleep(0.5)
        set_lights(0)
        time.sleep(0.5)
    
    time.sleep(10)
