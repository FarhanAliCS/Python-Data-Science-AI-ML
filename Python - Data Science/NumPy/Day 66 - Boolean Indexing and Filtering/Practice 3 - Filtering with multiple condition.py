import numpy as np

marks = np.array([45,67,89,32,76,95,50,84])

print("Student Marks between 50 Or above 50 :",marks[ (marks < 50) | (marks > 90)])
print("Marks greater then 60 and less then 90 :",marks[(marks > 60 ) & (marks < 90)])
print("Select marks that are not greater or equal to 70 :",marks[~(marks >= 70)])
print("Count of students marks between 60 and 90 :",np.sum((marks > 60) & (marks < 90 )))