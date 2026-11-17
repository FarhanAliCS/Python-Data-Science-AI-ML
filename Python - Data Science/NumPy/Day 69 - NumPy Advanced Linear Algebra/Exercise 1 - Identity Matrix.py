# Task 1 :- Create a 3x3 identity matrix using np.eye()
# Task 2 :- Create a Matrix A = [2,10][15 20]
# Task 3 :- Multiply A by a 2x2 identity matrix using @ .
import numpy as np
identity_matrix = np.eye(3,3)

A = np.array([
    [5 , 10],
    [15 , 20]
])

identity_matrix_2 = np.eye(2,2)

print("3x3 Indentity Matrix :\n",identity_matrix)
print(A @ identity_matrix_2)
