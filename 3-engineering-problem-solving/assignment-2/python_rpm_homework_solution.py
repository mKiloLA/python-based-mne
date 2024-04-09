# Import statements to make library methods available in this file
import csv
import math
import statistics
from matplotlib import pyplot

# Open and read data from a csv file into Python
with open("tire_rpm_homework.csv", "r", encoding="utf-8") as file_contents:
    csv_reader = csv.reader(file_contents, delimiter=",")
    rpm = []
    for rpm_value in next(csv_reader):
        # Turn the rpm_value (which would be a string) into an integer and add
        # it to a list of rpms
        rpm.append(int(rpm_value))

# Declare known constants and ask the user what diameter should be used for the tire
tire_diameter = input("What is the tire diameter?")
tire_circumference = tire_diameter * math.pi
inches_to_miles = 1 / 63360
min_per_hour = 60
conversion_factor = tire_circumference * inches_to_miles * min_per_hour

# Convert the rpm data to speed data and append to a list
speed = []
for rpm_value in rpm:
    speed.append(rpm_value * conversion_factor)

# Find the max speed
speed_max = max(speed)

# Find the minimum speed
speed_min = min(speed)

# Find the average of the data
speed_mean = statistics.mean(speed)

# Find the median value of the speed
speed_median = statistics.median(speed)

# Find the mode of the speed data
speed_mode = statistics.mode(speed)

# Print out the speed data with 0 decimal places of precision
print(f"The max speed was {speed_max:.0f}mph.")
print(f"The min speed was {speed_min:.0f}mph.")
print(f"The mean speed was {speed_mean:.0f}mph.")
print(f"The median speed was {speed_median:.0f}mph.")
print(f"The mode speed was {speed_mode:.0f}mph.")

# Create a time list that is the same length as the speed data
time = range(0, len(speed))

# Create a plot that is speed vs time with labels and a title
pyplot.plot(time, speed, label="Vehicle Speed")
pyplot.title("Vehicle Speed at a Given Time")
pyplot.xlabel("Time")
pyplot.ylabel("Speed (mph)")
pyplot.legend()
pyplot.show()


"""Extra Assignment

How long did it take this car with 22" wheels to go 0-60
if the sensor data was taken at 300Hz?
"""



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
