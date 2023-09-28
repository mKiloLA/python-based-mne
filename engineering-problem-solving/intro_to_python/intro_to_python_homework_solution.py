import csv
import math
import statistics
from matplotlib import pyplot

tire_diameter = 18
tire_circumference = tire_diameter * math.pi
inches_to_miles = 1 / 63360
min_per_hour = 60
conversion_factor = tire_circumference * inches_to_miles * min_per_hour

with open("tire_rpm_homework.csv", "r") as file_contents:
    csv_reader = csv.reader(file_contents, delimiter=",")
    for rpm_list in csv_reader:
        speed = [conversion_factor * int(x) for x in rpm_list]

speed_max = max(speed)
speed_min = min(speed)
speed_mean = statistics.mean(speed)
speed_median = statistics.median(speed)
speed_mode = statistics.mode(speed)

print("The max speed was {:.0f}mph.".format(speed_max))
print("The min speed was {:.0f}mph.".format(speed_min))
print("The mean speed was {:.0f}mph.".format(speed_mean))
print("The median speed was {:.0f}mph.".format(speed_median))
print("The mode speed was {:.0f}mph.".format(speed_mode))

time = [i for i in range(0, len(speed))]
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
        print("Time from 0-60mph: {:.2f}s".format(count/300))
        break
