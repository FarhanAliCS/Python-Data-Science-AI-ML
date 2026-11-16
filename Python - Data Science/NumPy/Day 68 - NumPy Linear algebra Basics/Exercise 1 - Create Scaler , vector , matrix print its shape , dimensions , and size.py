import numpy as np

scalar = np.array(25)
vector = np.array([10,20,30,40])
matrix = np.array([
    [10,20,30],
    [40,50,60]
])
print(":----- Scalar Info -----:")
print("Shape      :",scalar.shape)
print("Dimentions :",scalar.ndim)
print("Size       :",scalar.size)

print(":----- Vector Info -----:")
print("Shape      :",vector.shape)
print("Dimentions :",vector.ndim)
print("Size       :",vector.size)

print(":----- Matrix Info -----:")
print("Shape      :",matrix.shape)
print("Dimentions :",matrix.ndim)
print("Size       :",matrix.size)