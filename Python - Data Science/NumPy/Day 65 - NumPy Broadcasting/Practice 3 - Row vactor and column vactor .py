import numpy as np

row = np.array([[5,10,15,20]])
column = np.array([
    [2],
    [4],
    [6]
])
print("Row shape :",row.shape)
print("Coulumn Shape :",column.shape)
matrix = row + column

print(matrix)
print(matrix.shape)

matrix2 = row * column

print(matrix2.shape)
print(matrix2)

# Because the array is 1 row abd 3 column so the coulmn 1 elemnt + with all row 1 elemnts