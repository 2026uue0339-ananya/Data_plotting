import matplotlib.pyplot as plt

students = ["Ana", "Bhumi", "Sana", "Dip", "Mahi"]
marks = [75, 80, 99, 56, 89]

plt.bar(students, marks, color = 'green', width = 0.4)

plt.title("python examination marks")

plt.xlabel("Students")
plt.ylabel("Marks")

plt.ylim(0,100)

plt.show()