import csv
import matplotlib.pyplot as plt

months = []
sales = []

with open("sales.csv", "w", newline = "") as file:

    writer = csv.writer(file)

    writer.writerow(["Month", "Sales"])
    writer.writerow(["Jan", 12000])
    writer.writerow(["Feb", 15000])
    writer.writerow(["March", 13500])
    writer.writerow(["April", 18000])
    writer.writerow(["May", 21000])
    writer.writerow(["June", 19500])

    

with open("sales.csv", "r") as file:
    reader = csv.reader(file)
    next(reader) #skip header

    for row in reader:
        months.append(row[0])
        sales.append(int(row[1]))

plt.plot(months, sales, marker = '*')        

plt.xlabel("Months")
plt.ylabel("Sales ($)")
plt.grid()
plt.ylim(12000, 21000)
plt.tight_layout()
plt.show()

   