import matplotlib.pyplot as plt

Students_Attendence = [95, 90, 88, 89, 65, 5, 10, 70, 78, 55, 79, 2]
Months = ["Jan", "Feb", "March", "April", "May", "June", "July", "Aug", "Sept", "Oct", "Nov", "Dec"]

plt.plot(Months, Students_Attendence, marker = 'o')
plt.title("Students attendence analysis over months")
plt.xlabel("Months")
plt.ylabel("Attendence (%)")
plt.xticks(rotation = 90)
plt.grid()
plt.tight_layout()
plt.show()