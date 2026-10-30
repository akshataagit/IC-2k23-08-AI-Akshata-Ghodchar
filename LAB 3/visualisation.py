
import matplotlib.pyplot as plt

# Sample dataset
names = ['Amit', 'Riya', 'Rahul', 'Priya', 'Neha']
marks = [85, 90, 78, 95, 88]

# 1. Bar Chart
plt.figure(figsize=(7, 5))
plt.bar(names, marks)
plt.title("Student Marks - Bar Chart")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.savefig("outputs/bar_chart.png")
plt.show()

# 2. Line Chart
plt.figure(figsize=(7, 5))
plt.plot(names, marks, marker='o')
plt.title("Student Marks - Line Chart")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.savefig("outputs/line_chart.png")
plt.show()

# 3. Pie Chart
plt.figure(figsize=(7, 5))
plt.pie(
    marks,
    labels=names,
    autopct='%1.1f%%'
)
plt.title("Student Marks Distribution")
plt.savefig("outputs/pie_chart.png")
plt.show()

# 4. Scatter Plot
plt.figure(figsize=(7, 5))
plt.scatter(names, marks)
plt.title("Student Marks - Scatter Plot")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.savefig("outputs/scatter_plot.png")
plt.show()

# 5. Histogram
plt.figure(figsize=(7, 5))
plt.hist(marks, bins=5)
plt.title("Marks Distribution - Histogram")
plt.xlabel("Marks")
plt.ylabel("Frequency")
plt.savefig("outputs/histogram.png")
plt.show()

print("All Visualizations Created Successfully!")
