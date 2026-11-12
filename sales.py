import matplotlib.pyplot as plt

months = ["Jan", "Feb", "March", "April", "May", "June"]
items = ["Laptop", "Ac", "Gyzer", "Washing Machine", "Tv"]
sales = [[10, 4, 20, 45, 20],
         [18, 2,2, 10, 21], 
         [35, 23, 1, 21, 40],
         [50, 55, 1, 34, 21],
         [33, 56, 0, 21, 76],
         [12, 34, 0, 45, 67]]

plt.plot(items, sales[0], marker = 'o', label = "january") #for janury
plt.plot(items, sales[1], marker = 'o', label = "february") #for feb
plt.plot(items, sales[2], marker = 'o', label = "march") #marc
plt.plot(items, sales[3], marker = 'o', label = "april") #april
plt.plot(items, sales[4], marker = 'o', label = "may") #may
plt.plot(items, sales[5], marker = 'o', label = "june") #june



plt.grid(True)
plt.tight_layout()
plt.legend()
plt.xlabel("Items")
plt.ylabel("Sales")
plt.title("Sales Data over Months")
plt.show()
