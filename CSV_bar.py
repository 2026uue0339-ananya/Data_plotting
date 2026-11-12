import csv
import matplotlib.pyplot as plt
import numpy as np

students = []
python_marks = []
maths_marks = []
physics_marks = []

with open("students.csv", "w", newline = "") as file:

    writer = csv.writer(file)

    writer.writerow(["Students", "Python", "Maths", "Physics"])

    writer.writerow(["Anu", 85, 78, 82])
    writer.writerow(["Ravi", 72, 88, 75])
    writer.writerow(["Priya", 95, 92, 90])
    writer.writerow(["Amit", 68, 74, 71])

with open("students.csv", "r") as file:
    reader = csv.DictReader(file)
    

    for row in reader:

        students.append(row["Students"])
        python_marks.append(int(row["Python"]))
        maths_marks.append(int(row["Maths"]))
        physics_marks.append(int(row["Physics"]))

x = np.arange(len(students))
width = 0.15

plt.bar(x-width, python_marks, width, label="Python")
plt.bar(x, maths_marks, width, label = "Maths")
plt.bar(x+width, physics_marks, width, label="Physics")

plt.title("Students Marks Comparison")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.xticks(x, students, rotation = 45)
plt.ylim(0, 100)
plt.legend()
plt.show()
