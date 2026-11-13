import numpy as np

marks = np.array([75, 40, 90, 60, 85, 50])

print("Marks in ascinding order :" , np.sort(marks))
print("Marks in descending order :" , np.sort(marks)[::-1])
print("Find the index of sorted array :",np.argsort(marks))
indexes = np.argsort(marks)
print("Arrange the original array in ascending order using argsort() :",marks[indexes])