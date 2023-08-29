rpm = [x for x in range(0, 1430)] + [1430 for x in range(1000)] + [(1430 - x) for x in range(0, 1430)]
with open("vehicle_speed.csv", "w") as f:
    for i in range(len(rpm)):
        f.write(str(rpm[i]) + ',')