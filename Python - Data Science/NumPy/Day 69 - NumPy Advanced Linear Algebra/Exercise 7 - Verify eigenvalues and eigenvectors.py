import numpy as np

A = np.array([
    [4 , 0],
    [0 , 2]
])
eigen_value , eigen_vector = np.linalg.eig(A)
first_vector = eigen_vector[:,0]
eigen_value = eigen_value[0]

multiply_A_with_firstvector = A @ first_vector
firstvalue_firstvector = eigen_value * first_vector
print(np.allclose(multiply_A_with_firstvector , firstvalue_firstvector))