import numpy as np

A = np.array([
    [4 , 0],
    [0 , 2]
])
eigen_value , eigen_vector = np.linalg.eig(A)

print("Eigen Value  :",eigen_value)
print("Eigen Vector :",eigen_vector)