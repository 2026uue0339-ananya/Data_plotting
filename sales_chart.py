import matplotlib.pyplot as plt
import numpy as np

months = ["Jan", "Feb", "March", "April", "May", "June"]
items = ["Laptop", "Ac", "Gyzer", "Washing Machine", "Tv"]
sales = [[10, 4, 20, 45, 20],
         [18, 2,2, 10, 21], 
         [35, 23, 1, 21, 40],
         [50, 55, 1, 34, 21],
         [33, 56, 0, 21, 76],
         [12, 34, 0, 45, 67]]

x = np.arange(len(items))
width = 0.12

for i in range(len(months)):
    plt.bar(x + i*width, sales[i], width=width, label=months[i])

plt.xticks(x + width*2.5, items)

plt.legend()
plt.xlabel("Items")
plt.ylabel("Sales")
plt.title("Monthly Sales Data")
plt.tight_layout()
plt.show()