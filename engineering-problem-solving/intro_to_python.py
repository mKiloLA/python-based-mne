import csv
import statistics

with open("tire_rpm.csv", "r") as file_contents:
    csv_reader = csv.reader(file_contents, delimiter=",")
    for rpm_list in csv_reader:
        speed = [0.0595 * int(x) for x in rpm_list]

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
