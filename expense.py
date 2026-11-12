import matplotlib.pyplot as plt

months = ["Jan", "Feb", "March", "April", "May", "June",
           "July", "Aug", "Sept", "Oct", "Nov", "Dec"]

expenses = [12000, 15000, 13500, 18000, 21000, 19500,
            22000, 25000, 23000, 27000, 30000, 28000]

plt.pie(expenses, labels = months,
         autopct=lambda p: f'{p*sum(expenses)/100:.0f}',#to show the actual value
         startangle = 90)
plt.tight_layout()
plt.show()