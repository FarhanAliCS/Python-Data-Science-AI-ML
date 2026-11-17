import numpy as np

A = np.array([
    [4 , 7],
    [2 , 6]
])

inverse = np.linalg.inv(A)

A_x_inverse = A @ inverse

print("Inverse Matrix :\n",inverse)

print("A x inverse = \n",A_x_inverse)

#Result
# Inverse Matrix :
#  [[ 0.6 -0.7]
#  [-0.2  0.4]]
# A x inverse = 
#  [[ 1.00000000e+00 -1.11022302e-16]
#  [ 1.11022302e-16  1.00000000e+00]]