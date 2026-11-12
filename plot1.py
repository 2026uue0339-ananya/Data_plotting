import matplotlib.pyplot as plt

days = ["Mon", "Tues", "Wed", "Thrus", "Fri", "Sat"]
temp = [28, 30 , 29, 31, 32, 33]

plt.plot(days, temp, marker= 'o')
plt.xlabel("Days")
plt.ylabel("Temperature (°C)")
plt.title("Weekly Temperature Trend")
plt.grid(True)
plt.show()
