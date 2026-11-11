import numpy as np

marks = np.array([65,70,75,80,85,90])

print("--: Reshape the array :--")
matrix  = marks.reshape((2,3))
print(matrix)
print("--: Transpose array convert column into row and rows into column")
transpose = matrix.transpose()
print(transpose)

print("--: Ravel Operation Convert matrix into 1D array :--")
print(transpose.ravel())

print(" --: Resize Operation :-- ")
marks = np.array([65,70,75,80,85,90])
result=np.split(marks,3)
for arr in result:
    print(arr)
    print(arr.shape)
