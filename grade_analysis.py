import csv
import matplotlib.pyplot as plt

with open("students.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)

    for row in reader:
        name = row[0]
        python_marks = int(row[1])
        maths_marks = int(row[2])
        physics_marks = int(row[3])

          # Put the three subjects on the X-axis
        subjects = ["Python", "Maths", "Physics"]

        # Put the student's marks on the Y-axis
        marks = [python_marks, maths_marks, physics_marks]

        # Plot a separate line for each student
        plt.plot(subjects, marks, marker='o', label=name)

# Add legend to identify each student's line
plt.legend()

plt.xlabel("Subjects")
plt.ylabel("Marks")
plt.title("Student grade analysis")
plt.tight_layout() #for spacing properly
plt.grid(True)

plt.show()
