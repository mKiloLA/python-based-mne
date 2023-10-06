from machine import I2C, Pin
from vl53l1x import VL53L1X
import time
print("Making i2c object . . .")
i2c = I2C(0, sda=Pin(4), scl=Pin(5))

print("Attempting to connect to TOF sensor . . .")
time_of_flight = VL53L1X(i2c)
print("Connected. Loop beginning")

while True:
    data = time_of_flight.getDistance()
    print(f"Distance: {data} mm ")
    time.sleep_ms(1000)
