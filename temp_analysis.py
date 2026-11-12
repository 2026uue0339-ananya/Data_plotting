import csv

import matplotlib.pyplot as plt

with open("temperature.csv", "r")as file:
    reader = csv.reader(file)
    next(reader) #skip header

    days = []
    temp = []
    for row in reader:
        days.append(row[0])
        temp.append(float(row[1]))

plt.plot(days, temp, marker = 'o')
plt.xlabel("Days")
plt.ylabel("Temperature")
plt.title("Temperature Variation")
plt.xticks(rotation=45)
plt.grid()
plt.tight_layout()
plt.show()