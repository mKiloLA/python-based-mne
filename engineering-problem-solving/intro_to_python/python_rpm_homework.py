"""Python RPM Homework

CHANGE #1: Change the input file to the homework data set.
CHANGE #2: Change the tire diameter to utilize user input.
CHANGE #3: Change the print statements to have 0 decimal placs.
CHANGE #4: Anywhere there is a # COMMENT, leave a comment explaining 
           what the following lines of code do.
           
Additionally, there is a bonus assignment question at the bottom
of the file.
"""

# COMMENT
import csv
import math
import statistics
from matplotlib import pyplot

# COMMENT
with open("tire_rpm_homework.csv", "r", encoding="utf-8") as file_contents:
    csv_reader = csv.reader(file_contents, delimiter=",")
    rpm = []
    for rpm_row in csv_reader:
        for rpm_value in rpm_row:
            # COMMENT
            rpm.append(int(rpm_value))

# COMMENT
tire_diameter = 20
tire_circumference = tire_diameter * math.pi
inches_to_miles = 1 / 63360
min_per_hour = 60
conversion_factor = tire_circumference * inches_to_miles * min_per_hour

# COMMENT
speed = []
for rpm_value in rpm:
    speed.append(rpm_value * conversion_factor)

# COMMENT
speed_max = max(speed)

# COMMENT
speed_min = min(speed)

# COMMENT
speed_mean = statistics.mean(speed)

# COMMENT
speed_median = statistics.median(speed)

# COMMENT
speed_mode = statistics.mode(speed)

# COMMENT
print(f"The max speed was {speed_max:.2f}mph.")
print(f"The min speed was {speed_min:.2f}mph.")
print(f"The mean speed was {speed_mean:.2f}mph.")
print(f"The median speed was {speed_median:.2f}mph.")
print(f"The mode speed was {speed_mode:.2f}mph.")

# COMMENT
time = range(0, len(speed))

# COMMENT
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
