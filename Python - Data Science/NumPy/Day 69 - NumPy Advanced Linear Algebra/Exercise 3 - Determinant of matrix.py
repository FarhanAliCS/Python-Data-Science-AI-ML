import numpy as np

A = np.array([
    [5 , 2],
    [3 , 4]
])

determinant = np.linalg.det(A)
print("Determinant :",determinant)

# determinant = 5x4 - 2x3
# = 20 - 6
# = 14
# Determinant of a matrix a,b ,c,d is axd - bxc