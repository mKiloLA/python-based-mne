from drivers.hcsr04 import HCSR04
import time
sensor = HCSR04(trigger_pin=16, echo_pin=17)

start_time = time.ticks_ms()
while True:
    curr_time = time.ticks_ms()
    if time.ticks_diff(curr_time, start_time) > 1000:
        distance = sensor.distance_cm()
        print('Distance:', distance, 'cm')
        start_time = curr_time
