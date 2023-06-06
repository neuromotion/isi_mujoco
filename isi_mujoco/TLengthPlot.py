import numpy as np
import matplotlib
from matplotlib import pyplot as plt


# Graph layout sizing
plt.rcParams["figure.figsize"] = [7.00, 3.50]
plt.rcParams["figure.autolayout"] = True

with open('/Users/shanebarys/BortonLab/TLengthWrite.txt', 'r') as file:
    lines = file.readlines()

lengths_list = []
current_time = 0
times_list = []
muscle_name = ""

# Adding length data and time data to respective lists
for line in lines:
    # if line == 0:
    #     muscle_name = str(line.strip())
    # else:
        length = float(line.strip())
        lengths_list.append(length)
        times_list.append(current_time)
        current_time += 5

# Edit plot title here
plt.title("Chosen Tendon Activity")
plt.ylabel("Tendon Length")
plt.xlabel("Time Elapsed (ms)")

# Plotting x(time), y(lengths)
plt.plot(times_list, lengths_list)
plt.show()