import matplotlib.pyplot as plt 

activites = [ "Sleeping", "DoomScrolling", "Classes", "Assignment", "Tp", "Travelling"]
hours = [ 8, 1, 6, 4, 4,1]

plt.pie(hours, labels=activites, autopct="%1.1f%%", startangle=90)
plt.title("Time_Balance")
plt.show()