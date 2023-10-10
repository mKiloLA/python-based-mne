from machine import I2C, Pin
from drivers.vl6180x import VL6180X
import time

print("Making i2c object . . .")
i2c = I2C(0, sda=Pin(4), scl=Pin(5))

print("Attempting to connect to TOF sensor . . .")
time_of_flight = VL6180X(i2c)
print("Connected. Loop beginning")

while True:
    if time_of_flight.rangeDataReady():
        data = time_of_flight.readRangeNonBlocking()
        print(f"Distance: {data} mm ")
    time.sleep_ms(1000)
