import numpy as np

A = np.array([
    [10,20,30],
    [40,50,60]
])

transpose = A.T
transpose2 = A.transpose()

print("Original Shape :",A.shape)
print("Tranposed 1 and 2 shape :",transpose.shape , transpose2.shape)

