import numpy as np

A = np.array([
    [1,2],
    [3,4]
])

print("Rank of A :",np.linalg.matrix_rank(A))

B = np.array([
    [1,2],
    [2,4]
])

print("Rank of B :",np.linalg.matrix_rank(B))

# Their Ranks are different because they the A matrix is not = the multiplication of first matrix and second are the multiplication of first row