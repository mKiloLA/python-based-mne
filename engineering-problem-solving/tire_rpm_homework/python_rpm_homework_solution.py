import csv
import math
import statistics
from matplotlib import pyplot

tire_diameter = int(input("Tire Diameter: "))
tire_circumference = tire_diameter * math.pi
inches_to_miles = 1 / 63360
min_per_hour = 60
conversion_factor = tire_circumference * inches_to_miles * min_per_hour

with open("tire_rpm_homework.csv", "r", encoding="utf-8") as file_contents:
    csv_reader = csv.reader(file_contents, delimiter=",")
    for rpm_list in csv_reader:
        speed = [conversion_factor * int(x) for x in rpm_list]

speed_max = max(speed)
speed_min = min(speed)
speed_mean = statistics.mean(speed)
speed_median = statistics.median(speed)
speed_mode = statistics.mode(speed)

print(f"The max speed was {speed_max:.0f}mph.")
print(f"The min speed was {speed_min:.0f}mph.")
print(f"The mean speed was {speed_mean:.0f}mph.")
print(f"The median speed was {speed_median:.0f}mph.")
print(f"The mode speed was {speed_mode:.0f}mph.")

time = range(0, len(speed))
pyplot.plot(time, speed, label="Vehicle Speed")
pyplot.title("Vehicle Speed at a Given Time")
pyplot.xlabel("Time")
pyplot.ylabel("Speed (mph)")
pyplot.legend()
pyplot.show()


# Extra Credit Question Solution
# How long did it take this car with 22" wheels to go 0-60
# if the sensor data was taken at 300Hz
speed = [(22/18)*x for x in speed]

# Graphically
time = [(i / 300) for i in range(0, len(speed))]
pyplot.plot(time, speed, label="Vehicle Speed")
pyplot.title("Vehicle Speed at a Given Time")
pyplot.xlabel("Time (sec)")
pyplot.ylabel("Speed (mph)")
pyplot.legend()
pyplot.show()

# Numerically
for count, mph in enumerate(speed):
    if mph >= 60:
        print(f"Time from 0-60mph: {(count/300):.2f}s")
        break
