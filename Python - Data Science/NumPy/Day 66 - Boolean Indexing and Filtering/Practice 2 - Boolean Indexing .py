import numpy as np

marks = np.array([45,67,89,32,76,95,50,84])

greater_equal_70 = marks >= 70
less_50 = marks < 50
marks_between_50_and_80 = (marks >= 50) & (marks <=80)

print("Marks greater or equal to 70 :",marks[greater_equal_70])
print("Marks less then 50 :",marks[less_50])
print("Marks between 50 and 80 :",marks[marks_between_50_and_80])
print("Student count whose marks 70 or above :" , np.sum(marks >= 70))
