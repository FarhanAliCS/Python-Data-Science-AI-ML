import numpy as np

marks = np.array([45, 67, 89, 32, 76, 95, 50, 84, 67, 90])

passed_students = marks[marks >= 50]
count_passed_student = len(passed_students)
values , frequencies = np.unique(marks , return_counts=True)
index=np.argmax(frequencies)
marks_descending_order = np.sort(marks)[::-1]
index_marks_greater_80 = np.where(marks > 80)

print("   -----: Student Marks Analyzer :-----   ")
print("Passed students            :", passed_students)
print("Count of passed students   :",count_passed_student)
print("Marks and their frequecies :",values , frequencies)
print("Most occuring marks        :",values[index])
print("Marks in Descending order  :",marks_descending_order)
print("Greater then 80 marks indexes :",index_marks_greater_80)

